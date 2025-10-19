#!/usr/bin/env python3
# Adzuna-powered broad search for internships in Boston or Remote (US).
# Get free keys: https://developer.adzuna.com/overview
#
# Usage:
#   export ADZUNA_APP_ID=xxxxx
#   export ADZUNA_APP_KEY=yyyyy
#   python adzuna_report.py --what "intern systems OR infrastructure OR backend OR reliability OR compiler OR quant OR simulation OR modeling OR 'data infrastructure' OR 'ml systems'" --location "Boston, MA" --remote --out ./reports

import argparse, datetime as dt, os, re
import requests

API_BASE = "https://api.adzuna.com/v1/api/jobs/us/search/1"

def format_location(location: str) -> str:
    """Format location string with proper separators and truncation."""
    if not location:
        return location
    
    # Preserve "Remote in USA" and "Remote in Canada" exactly as they are
    location = location.replace('Remote in USA', '<<<REMOTE_USA>>>')
    location = location.replace('Remote in Canada', '<<<REMOTE_CANADA>>>')
    
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

def fetch_adzuna(what: str, where: str = "Boston, MA", max_days_old: int = 7, remote: bool = False, results_per_page: int = 50):
    app_id = os.environ.get("ADZUNA_APP_ID")
    app_key = os.environ.get("ADZUNA_APP_KEY")
    if not app_id or not app_key:
        raise RuntimeError("Set ADZUNA_APP_ID and ADZUNA_APP_KEY in your environment")

    params = {
        "app_id": app_id,
        "app_key": app_key,
        "what": what,
        "where": where,
        "results_per_page": results_per_page,
        "content-type": "application/json",
        "max_days_old": max_days_old,
    }
    if remote:
        params["remote"] = 1

    r = requests.get(API_BASE, params=params, timeout=20)
    r.raise_for_status()
    return r.json()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--what", default='intern OR internship OR co-op OR coop OR student OR graduate OR "new grad" OR entry OR junior OR systems OR infrastructure OR backend OR "core systems" OR frontend OR "front end" OR "full stack" OR web OR mobile OR reliability OR "site reliability" OR sre OR devops OR cloud OR security OR qa OR "quality assurance" OR support OR IT OR compiler OR compilers OR algorithm OR algorithms OR quant OR quantitative OR simulation OR modeling OR "data infrastructure" OR "data platform" OR analytics OR "data science" OR "ml systems" OR "machine learning systems" OR "ml infra" OR "ml platform" OR product OR UX OR UI OR design OR research OR campus OR university OR fall OR spring OR summer')
    ap.add_argument("--location", default="Boston, MA")
    ap.add_argument("--remote", action="store_true")
    ap.add_argument("--max-days-old", type=int, default=7)
    args = ap.parse_args()

    data = fetch_adzuna(args.what, args.location, args.max_days_old, args.remote)
    results = data.get("results", [])
    print(f"Found {len(results)} results from Adzuna.")

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
    
    # Prepare table rows (excluding duplicates)
    table_rows = []
    added_count = 0
    skipped_count = 0
    for it in results:
        # Extra strict internship/co-op filter
        title = (it.get("title", "") or "").lower()
        desc = (it.get("description", "") or "").lower()
        if not ("intern" in title or "internship" in title or "co-op" in title or "co op" in title or "intern" in desc or "internship" in desc or "co-op" in desc or "co op" in desc):
            continue
        
        url = it.get("redirect_url", "")
        # Skip if URL already exists in README
        if url and url in existing_urls:
            skipped_count += 1
            continue
        
        company = (it.get("company") or {}).get("display_name", "")
        job_title = (it.get("title", "") or "").replace("|", r"\|")
        location = format_location((it.get("location") or {}).get("display_name", ""))
        # Format date posted as MM/DD/YYYY
        raw_date = it.get("created", "")
        date_posted = ""
        if raw_date:
            try:
                from datetime import datetime
                date_posted = datetime.fromisoformat(raw_date[:10]).strftime("%m/%d/%Y")
            except Exception:
                date_posted = raw_date
        # Use HTML link with target="_blank" to open in new tab
        apply_link = f'<a href="{url}" target="_blank">APPLY</a>' if url else ""
        table_rows.append(f"| {company} | {job_title} | {location} | {date_posted} | {apply_link} |")
        added_count += 1

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
    
    print(f"README.md: Added {added_count} new jobs, skipped {skipped_count} duplicates.")

if __name__ == "__main__":
    main()
