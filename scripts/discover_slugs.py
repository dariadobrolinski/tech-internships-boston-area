import os, re, time, argparse, requests, yaml
from pathlib import Path
from urllib.parse import urlparse
from datetime import datetime

GH_HOST = "boards.greenhouse.io"
LEVER_HOST = "jobs.lever.co"
SERPAPI_ENDPOINT = "https://serpapi.com/search.json"

def serpapi_search(q, api_key, num=10):
    params = {"engine": "google", "q": q, "api_key": api_key, "num": num, "hl": "en"}
    r = requests.get(SERPAPI_ENDPOINT, params=params, timeout=20)
    r.raise_for_status()
    return r.json()

def extract_slug(url, host):
    try:
        p = urlparse(url)
        if p.netloc != host:
            return None
        parts = [seg for seg in p.path.split("/") if seg]
        if not parts:
            return None
        return parts[0]
    except Exception:
        return None

def validate_greenhouse(slug):
    url = f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true"
    r = requests.get(url, timeout=20)
    return r.status_code == 200

def validate_lever(slug):
    url = f"https://api.lever.co/v0/postings/{slug}?mode=json"
    r = requests.get(url, timeout=20)
    return r.status_code == 200

def merge_companies(path, gh_slugs, lever_slugs):
    existing = {"companies": [], "boston_locations": [], "include_remote": False, "out_dir": "./reports"}
    if Path(path).exists():
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            if isinstance(data, dict):
                existing = data

    names = {(c.get("provider"), c.get("slug")) for c in existing.get("companies", [])}
    new_companies = list(existing.get("companies", []))

    for slug in sorted(gh_slugs):
        key = ("greenhouse", slug)
        if key not in names:
            new_companies.append({"name": slug.capitalize(), "provider": "greenhouse", "slug": slug, "include_keywords": [], "exclude_keywords": []})
            names.add(key)

    for slug in sorted(lever_slugs):
        key = ("lever", slug)
        if key not in names:
            new_companies.append({"name": slug.capitalize(), "provider": "lever", "slug": slug, "include_keywords": [], "exclude_keywords": []})
            names.add(key)

    existing["companies"] = new_companies
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(existing, f, sort_keys=False)
    return len(new_companies)

def fetch_greenhouse_jobs(slug):
    """Fetch jobs from Greenhouse API."""
    url = f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true"
    r = requests.get(url, timeout=10)
    if r.status_code != 200:
        return []
    data = r.json()
    return data.get("jobs", [])

def fetch_lever_jobs(slug):
    """Fetch jobs from Lever API."""
    url = f"https://api.lever.co/v0/postings/{slug}?mode=json"
    r = requests.get(url, timeout=10)
    if r.status_code != 200:
        return []
    return r.json()

def normalize_greenhouse_job(job, company_name):
    """Normalize a Greenhouse job to a common format."""
    title = job.get("title", "") or ""
    url = job.get("absolute_url", "") or ""
    loc = ""
    loc_obj = job.get("location")
    if isinstance(loc_obj, dict):
        loc = loc_obj.get("name", "") or ""
    elif isinstance(loc_obj, str):
        loc = loc_obj
    updated_at = job.get("updated_at") or job.get("created_at") or ""
    return {
        "company": company_name,
        "title": title,
        "location": loc,
        "date_posted": updated_at,
        "url": url
    }

def normalize_lever_job(job, company_name):
    """Normalize a Lever job to a common format."""
    title = job.get("text", "") or ""
    url = job.get("hostedUrl") or job.get("applyUrl") or ""
    loc = ""
    cats = job.get("categories")
    if isinstance(cats, dict):
        loc = cats.get("location", "") or ""
    elif isinstance(job.get("workplaceType"), str):
        loc = job.get("workplaceType") or ""
    updated_at = job.get("createdAt") or job.get("updatedAt") or ""
    return {
        "company": company_name,
        "title": title,
        "location": loc,
        "date_posted": updated_at,
        "url": url
    }

def append_jobs_to_readme(jobs_to_add):
    """Append new jobs to README.md in the same format as job_report.py."""
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    
    # If README.md doesn't exist, create with header and table
    if not Path(readme_path).exists():
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write("# Job Listings\n\n")
            f.write("| Company Name | Job Title | Location | Date Posted | APPLY |\n")
            f.write("|---|---|---|---|---|\n")
    
    # Read existing README.md and extract existing URLs
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_lines = f.readlines()
    
    # Extract all existing URLs from the README
    import re
    existing_urls = set()
    for line in readme_lines:
        # Match URLs in [APPLY](url) format
        matches = re.findall(r'\[APPLY\]\((https?://[^\)]+)\)', line)
        existing_urls.update(matches)
    
    # Prepare table rows (excluding duplicates)
    table_rows = []
    added_count = 0
    skipped_count = 0
    for job in jobs_to_add:
        url = job.get("url", "")
        
        # Skip if URL already exists in README
        if url and url in existing_urls:
            skipped_count += 1
            continue
        
        company = job.get("company", "")
        job_title = (job.get("title", "") or "").replace("|", "\\|")
        location = (job.get("location") or "").replace("|", "\\|")
        
        # Format date posted as MM/DD/YYYY
        raw_date = job.get("date_posted") or ""
        date_posted = ""
        if raw_date:
            try:
                # Try parsing ISO format
                date_posted = datetime.fromisoformat(raw_date[:10]).strftime("%m/%d/%Y")
            except Exception:
                date_posted = raw_date
        
        apply_link = f"[APPLY]({url})" if url else ""
        table_rows.append(f"| {company} | {job_title} | {location} | {date_posted} | {apply_link} |")
        added_count += 1

    if not table_rows:
        if skipped_count > 0:
            print(f"All {skipped_count} jobs were already in README.md (no duplicates added)")
        return

    # Find where the table ends
    table_start = None
    for i, line in enumerate(readme_lines):
        if line.strip().startswith("|---|---|---|---|---|"):
            table_start = i
            break
    
    # If table exists, append rows after it
    if table_start is not None:
        # Find last row in table
        last_row = table_start + 1
        while last_row < len(readme_lines) and readme_lines[last_row].startswith("|"):
            last_row += 1
        # Insert new rows after last_row
        new_lines = readme_lines[:last_row] + [row + "\n" for row in table_rows] + readme_lines[last_row:]
    else:
        # No table found, add header and table
        new_lines = ["# Job Listings\n\n", "| Company Name | Job Title | Location | Date Posted | APPLY |\n", "|---|---|---|---|---|\n"] + [row + "\n" for row in table_rows] + readme_lines
    
    # Write back to README.md
    with open(readme_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    
    print(f"Added {added_count} new jobs to README.md, skipped {skipped_count} duplicates")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cities", default="Boston,Cambridge,Somerville,Quincy,Newton,Brookline,Waltham,Watertown,Burlington,Lexington,Needham")
    ap.add_argument("--keywords", default="intern internship co-op coop student graduate new grad entry junior software engineer backend infrastructure systems reliability compiler quant data platform analytics data science ml ai frontend front end full stack web mobile devops cloud security qa quality assurance support IT product UX UI design research campus university fall spring summer")
    ap.add_argument("--max", type=int, default=100)
    ap.add_argument("--config", default="config/companies.yml")
    args = ap.parse_args()

    api_key = os.environ.get("SERPAPI_KEY")
    if not api_key:
        raise SystemExit("Set SERPAPI_KEY in your environment")

    cities = [c.strip() for c in args.cities.split(",") if c.strip()]
    keywords = [k.strip() for k in args.keywords.split() if k.strip()]

    gh_slugs_found, lever_slugs_found = set(), set()
    queries = []
    for city in cities:
        for kw in keywords[:10]:
            queries.append(f'site:{GH_HOST} "{city}" {kw}')
            queries.append(f'site:{LEVER_HOST} "{city}" {kw}')
    queries = list(dict.fromkeys(queries))[:args.max]

    for q in queries:
        data = serpapi_search(q, api_key, num=10)
        for res in data.get("organic_results", []):
            link = res.get("link")
            if not link:
                continue
            slug = extract_slug(link, GH_HOST)
            if slug and validate_greenhouse(slug):
                gh_slugs_found.add(slug)
                continue
            slug = extract_slug(link, LEVER_HOST)
            if slug and validate_lever(slug):
                lever_slugs_found.add(slug)
                continue
        time.sleep(0.8)

    total = merge_companies(args.config, gh_slugs_found, lever_slugs_found)
    print("Greenhouse slugs:", sorted(gh_slugs_found))
    print("Lever slugs:", sorted(lever_slugs_found))
    print(f"Updated {args.config} with {total} total companies.")
    
    # Fetch jobs from newly discovered companies and append to README
    print("\nFetching jobs from newly discovered companies...")
    all_jobs = []
    
    for slug in sorted(gh_slugs_found):
        try:
            print(f"  Fetching Greenhouse jobs from {slug}...")
            jobs = fetch_greenhouse_jobs(slug)
            for job in jobs:
                normalized = normalize_greenhouse_job(job, slug.capitalize())
                all_jobs.append(normalized)
        except Exception as e:
            print(f"  ⚠️  Failed to fetch jobs from {slug}: {e}")
    
    for slug in sorted(lever_slugs_found):
        try:
            print(f"  Fetching Lever jobs from {slug}...")
            jobs = fetch_lever_jobs(slug)
            for job in jobs:
                normalized = normalize_lever_job(job, slug.capitalize())
                all_jobs.append(normalized)
        except Exception as e:
            print(f"  ⚠️  Failed to fetch jobs from {slug}: {e}")
    
    if all_jobs:
        append_jobs_to_readme(all_jobs)
    else:
        print("No jobs found from newly discovered companies.")

if __name__ == "__main__":
    main()
