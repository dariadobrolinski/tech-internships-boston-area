import argparse
import datetime as dt
import logging
import os
import re
import sys
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import requests
from requests.adapters import HTTPAdapter, Retry

# ---------- Logging ----------
logging.basicConfig(
    level=os.environ.get("LOGLEVEL", "INFO"),
    format="%(levelname)s: %(message)s"
)

# ---------- Location Formatting ----------
def format_location(location: str) -> str:
    """Format location string with proper separators and truncation."""
    if not location:
        return location
    
    # Preserve "Remote in USA" and "Remote in Canada" exactly as they are
    location = location.replace('Remote in USA', '<<<REMOTE_USA>>>')
    location = location.replace('Remote in Canada', '<<<REMOTE_CANADA>>>')
    
    # Handle concatenated state/location names without spaces
    # e.g., "NHMississippiTennessee" -> "NH, Mississippi, Tennessee"
    # Split on patterns where a lowercase letter is followed by an uppercase letter or full state name
    location = re.sub(r'([a-z])([A-Z][a-z]{3,})', r'\1, \2', location)  # lowercase followed by capitalized word
    location = re.sub(r'([A-Z]{2})([A-Z][a-z]{3,})', r'\1, \2', location)  # 2-letter state code followed by full name
    
    # Add commas between locations that are missing them
    location = re.sub(r'([A-Z]{2})([A-Z]{2,}[a-z])', r'\1, \2', location)
    location = re.sub(r'([A-Z]{2})([A-Z]{3,})', r'\1, \2', location)
    location = re.sub(r'([A-Z]{2})([A-Z][a-z])', r'\1, \2', location)
    location = re.sub(r'([a-z])([A-Z][a-z])', r'\1, \2', location)
    location = re.sub(r'(Remote in [A-Z]{2,})([A-Z])', r'\1, \2', location)
    location = re.sub(r'(Remote in [A-Za-z\s]+?)([A-Z][a-z]+, [A-Z]{2})', r'\1, \2', location)
    location = re.sub(r'(\d+ locations)([A-Z])', r'\1, \2', location)
    
    # Restore preserved patterns
    location = location.replace('<<<REMOTE_USA>>>', 'Remote in USA')
    location = location.replace('<<<REMOTE_CANADA>>>', 'Remote in Canada')
    
    locations = re.split(r'[,;]', location)
    locations = [loc.strip() for loc in locations if loc.strip()]
    
    # Remove duplicates while preserving order
    seen = set()
    unique_locations = []
    for loc in locations:
        loc_lower = loc.lower()
        if loc_lower not in seen:
            seen.add(loc_lower)
            unique_locations.append(loc)
    locations = unique_locations
    
    # If too many locations or too long, truncate and add line break
    if len(locations) > 3 or len(', '.join(locations)) > 50:
        kept_locations = []
        total_length = 0
        
        for loc in locations[:3]:
            if total_length + len(loc) > 50 and kept_locations:
                break
            kept_locations.append(loc)
            total_length += len(loc) + 2
        
        result = ', '.join(kept_locations)
        
        if len(locations) > len(kept_locations):
            remaining = len(locations) - len(kept_locations)
            result += f'<br>+{remaining} more'
        
        return result
    
    return ', '.join(locations)

# ---------- HTTP with retries ----------
def session_with_retries(total=2, backoff=0.3) -> requests.Session:
    s = requests.Session()
    retries = Retry(
        total=total,
        backoff_factor=backoff,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"]
    )
    s.mount("http://", HTTPAdapter(max_retries=retries))
    s.mount("https://", HTTPAdapter(max_retries=retries))
    s.headers.update({"User-Agent": "job-reporter/1.1"})
    return s

HTTP = session_with_retries()

# ---------- Models ----------
@dataclass
class Company:
    name: str
    provider: str   # "greenhouse" | "lever"
    slug: str
    include_keywords: List[str]
    exclude_keywords: List[str]

@dataclass
class Config:
    companies: List[Company]
    boston_locations: List[str]
    include_remote: bool
    out_dir: str

# ---------- Defaults ----------
ROLE_KEYWORDS_DEFAULT = [
    "intern", "internship", "co-op", "coop", "student", "graduate", "new grad", "entry", "junior",
    "systems", "infrastructure", "backend", "core systems", "frontend", "front end", "full stack", "web", "mobile",
    "reliability", "site reliability", "sre", "devops", "cloud", "security", "qa", "quality assurance", "support", "IT",
    "compiler", "compilers", "algorithm", "algorithms", "quant", "quantitative", "simulation", "modeling",
    "data infrastructure", "data platform", "analytics", "data science", "ml systems", "machine learning systems", "ml infra", "ml platform",
    "product", "UX", "UI", "design", "research", "campus", "university", "fall", "spring", "summer"
    "platform"
]

EXCLUDE_TITLE_TERMS = [
    # leadership/seniority signals to exclude
    "senior", "sr", "staff", "principal", "lead", "manager", "director", "head", "vp", "chief"
]

# ---------- Config loader ----------
def load_config(path: str, include_remote_flag: bool, out_dir_cli: Optional[str]) -> Config:
    import yaml
    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    companies = []
    for c in raw.get("companies", []):
        companies.append(Company(
            name=c["name"],
            provider=c["provider"],
            slug=c["slug"],
            include_keywords=[k.lower() for k in c.get("include_keywords", [])],
            exclude_keywords=[k.lower() for k in c.get("exclude_keywords", [])],
        ))

    boston_locations = [loc.lower() for loc in raw.get("boston_locations", [
        "boston", "cambridge", "somerville", "lexington", "needham",
        "waltham", "watertown", "brookline", "newton", "burlington", "quincy"
    ])]

    include_remote = include_remote_flag or bool(raw.get("include_remote", False))
    out_dir = out_dir_cli or raw.get("out_dir", "./reports")
    os.makedirs(out_dir, exist_ok=True)
    return Config(companies=companies, boston_locations=boston_locations, include_remote=include_remote, out_dir=out_dir)

# ---------- Providers ----------
def fetch_greenhouse(company_slug: str) -> List[Dict[str, Any]]:
    url = f"https://boards-api.greenhouse.io/v1/boards/{company_slug}/jobs?content=true"
    r = HTTP.get(url, timeout=10)
    if r.status_code != 200:
        raise RuntimeError(f"Greenhouse {company_slug} HTTP {r.status_code}: {r.text[:300]}")
    data = r.json()
    return data.get("jobs", [])

def fetch_lever(company_slug: str) -> List[Dict[str, Any]]:
    url = f"https://api.lever.co/v0/postings/{company_slug}?mode=json"
    r = HTTP.get(url, timeout=10)
    if r.status_code != 200:
        raise RuntimeError(f"Lever {company_slug} HTTP {r.status_code}: {r.text[:300]}")
    return r.json()

# ---------- Normalization ----------
def normalize_greenhouse(job: Dict[str, Any]) -> Dict[str, Any]:
    title = job.get("title", "") or ""
    url = job.get("absolute_url", "") or ""
    loc = ""
    loc_obj = job.get("location")
    if isinstance(loc_obj, dict):
        loc = loc_obj.get("name", "") or ""
    elif isinstance(loc_obj, str):
        loc = loc_obj
    updated_at = job.get("updated_at") or job.get("created_at")
    desc = (job.get("content") or "")  # HTML or text
    return {"title": title, "url": url, "location": loc, "updated_at": updated_at, "desc": desc}

def normalize_lever(job: Dict[str, Any]) -> Dict[str, Any]:
    title = job.get("text", "") or ""
    url = job.get("hostedUrl") or job.get("applyUrl") or ""
    loc = ""
    cats = job.get("categories")
    if isinstance(cats, dict):
        loc = cats.get("location", "") or ""
    elif isinstance(job.get("workplaceType"), str):
        loc = job.get("workplaceType") or ""
    updated_at = job.get("createdAt") or job.get("updatedAt")
    desc = job.get("descriptionPlain") or job.get("description") or ""
    return {"title": title, "url": url, "location": loc, "updated_at": updated_at, "desc": desc}

# ---------- Filters ----------
def location_matches(loc: str, boston_locations: List[str], include_remote: bool) -> bool:
    l = (loc or "").lower()
    if any(city in l for city in boston_locations):
        return True
    if include_remote:
        # Check for remote indicators, but exclude specific non-MA cities
        # Exclude other US states/cities first
        non_ma_cities = [
            'denver', 'colorado', ', co,', ', co ', 
            'tempe', 'arizona', ', az,', ', az ',
            'new york', ', ny,', ', ny ', 'nyc',
            'san francisco', 'california', ', ca,', ', ca ',
            'seattle', 'washington', ', wa,', ', wa ',
            'austin', 'texas', ', tx,', ', tx ',
            'chicago', 'illinois', ', il,', ', il ',
        ]
        # If it contains a non-MA city/state, reject it
        if any(city in l for city in non_ma_cities):
            return False
        # Now check for remote keywords
        if any(rem in l for rem in ("remote", "anywhere", "distributed", "remote in usa", "remote in us", "united states remote")):
            return True
    return False

def title_matches_keywords(title: str, include_keywords: List[str], exclude_keywords: List[str]) -> bool:
    t = (title or "").lower()
    include = include_keywords or ROLE_KEYWORDS_DEFAULT
    if not any(k in t for k in include):
        return False
    if any(k in t for k in (exclude_keywords or [])):
        return False
    return True

def is_intern_role(title: str, desc: str = "") -> bool:
    """
    Require internship signals in title/description and exclude senior/lead/etc.
    """
    t = (title or "").lower()
    d = (desc or "").lower()

    # Must contain intern/internship in title OR description
    looks_intern = ("intern" in t) or ("internship" in t) or ("intern" in d) or ("internship" in d)
    if not looks_intern:
        return False

    # Exclude seniority signals in title
    if any(bad in t for bad in EXCLUDE_TITLE_TERMS):
        return False

    return True

# ---------- Report ----------
def format_md(date_str: str, items: List[Dict[str, Any]]) -> str:
    header = f"# Boston/Remote Internship Report — {date_str}\n\n"
    if not items:
        return header + "_No matching postings found today._\n"
    lines = [
        header,
        "| Title | Company | Location | Source | Updated |",
        "|---|---|---|---|---|",
    ]
    for it in items:
        company = it.get("company", "")
        title = (it.get("title", "") or "").replace("|", "\\|")
        location = format_location((it.get("location") or "")).replace("|", "\\|")
        source = it.get("source", "")
        updated = it.get("updated_at") or ""
        url = it.get("url", "")
        link = f"[{title}]({url})" if url else title
        lines.append(f"| {link} | {company} | {location} | {source} | {updated} |")
    return "\n".join(lines) + "\n"

def send_email_if_configured(subject: str, body_md: str) -> bool:
    host = os.environ.get("JOB_REPORT_SMTP_HOST")
    port = int(os.environ.get("JOB_REPORT_SMTP_PORT", "587"))
    user = os.environ.get("JOB_REPORT_SMTP_USER")
    pwd  = os.environ.get("JOB_REPORT_SMTP_PASS")
    to   = os.environ.get("JOB_REPORT_TO")
    from_addr = os.environ.get("JOB_REPORT_FROM", user)

    if not all([host, user, pwd, to, from_addr]):
        return False  # not configured

    import smtplib
    from email.mime.text import MIMEText

    msg = MIMEText(body_md, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(user, pwd)
        server.send_message(msg)
    return True

# ---------- Main ----------
def main():
    parser = argparse.ArgumentParser(description="Daily Boston internship report (Greenhouse/Lever).")
    parser.add_argument("--config", default="config/companies.yml", help="Path to YAML config file")
    parser.add_argument("--include-remote", action="store_true", help="Include remote U.S. roles")
    parser.add_argument("--out", dest="out_dir", default=None, help="Output directory for reports")
    args = parser.parse_args()

    cfg = load_config(args.config, args.include_remote, args.out_dir)

    today = dt.date.today().isoformat()
    results: List[Dict[str, Any]] = []

    total_companies = len(cfg.companies)
    for idx, c in enumerate(cfg.companies, 1):
        print(f"[{idx}/{total_companies}] Fetching {c.name} ({c.provider})...", flush=True)
        try:
            if c.provider == "greenhouse":
                jobs = fetch_greenhouse(c.slug)
                normalized = [normalize_greenhouse(j) for j in jobs]
            elif c.provider == "lever":
                jobs = fetch_lever(c.slug)
                normalized = [normalize_lever(j) for j in jobs]
            else:
                logging.warning("Skipping %s: unsupported provider %s", c.name, c.provider)
                continue

            for job in normalized:
                if not location_matches(job.get("location", "") or "", cfg.boston_locations, cfg.include_remote):
                    continue
                if not title_matches_keywords(job.get("title", ""), c.include_keywords, c.exclude_keywords):
                    continue
                if not is_intern_role(job.get("title", ""), job.get("desc", "")):
                    continue

                results.append({
                    **job,
                    "company": c.name,
                    "source": c.provider,
                })

        except Exception as e:
            logging.warning("%s fetch failed: %s", c.name, e)
            print(f"  ⚠️  {c.name} failed: {e}", flush=True)

    # Sort newest first (by provider timestamp if present)
    def sort_key(it: Dict[str, Any]):
        updated = it.get("updated_at")
        if not isinstance(updated, str):
            updated = str(updated) if updated is not None else ""
        return (updated, it.get("company") or "")

    results_sorted = sorted(results, key=sort_key, reverse=True)

    # --- Append to README.md ---
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    
    # If README.md doesn't exist, create with header and table
    if not os.path.exists(readme_path):
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
        # Match URLs in [APPLY](url) format (old markdown style)
        matches = re.findall(r'\[APPLY\]\((https?://[^\)]+)\)', line)
        existing_urls.update(matches)
        # Match URLs in HTML <a href="url"> format (new HTML style)
        matches = re.findall(r'<a href="(https?://[^"]+)"', line)
        existing_urls.update(matches)
    
    # Prepare table rows (internships only, with date posted, excluding duplicates)
    table_rows = []
    added_count = 0
    skipped_count = 0
    for it in results_sorted:
        # Extra strict internship/co-op filter
        title = (it.get("title", "") or "").lower()
        desc = (it.get("desc", "") or "").lower()
        if not ("intern" in title or "internship" in title or "co-op" in title or "co op" in title or "intern" in desc or "internship" in desc or "co-op" in desc or "co op" in desc):
            continue
        
        url = it.get("url", "")
        # Skip if URL already exists in README
        if url and url in existing_urls:
            skipped_count += 1
            continue
        
        company = it.get("company", "")
        job_title = (it.get("title", "") or "").replace("|", "\\|")
        location = format_location((it.get("location") or "")).replace("|", "\\|")
        # Format date posted as MM/DD/YYYY
        raw_date = it.get("updated_at") or it.get("created_at") or ""
        date_posted = ""
        if raw_date:
            try:
                # Try parsing ISO format
                from datetime import datetime
                date_posted = datetime.fromisoformat(raw_date[:10]).strftime("%m/%d/%Y")
            except Exception:
                date_posted = raw_date
        # Format apply link
        apply_link = f'[APPLY]({url})' if url else ""
        table_rows.append(f"| {company} | {job_title} | {location} | {date_posted} | {apply_link} |")
        added_count += 1

    # Find where the table ends
    table_start = None
    for i, line in enumerate(readme_lines):
        # Match both old and new table separator formats
        if line.strip().startswith("|---|---|---|---|") and "---" in line:
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

    print(f"Found {len(results_sorted)} total jobs from {total_companies} companies.")
    print(f"README.md: Added {added_count} new jobs, skipped {skipped_count} duplicates.")

if __name__ == "__main__":
    main()
