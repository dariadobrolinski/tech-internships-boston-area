#!/usr/bin/env python3
"""
SimplifyJobs Summer2026-Internships Scraper
Fetches tech internship listings from the SimplifyJobs GitHub repo and filters
for Boston area and remote positions.

Usage:
    python simplify_scraper.py --out ./reports
"""

import argparse
import datetime as dt
import logging
import os
import re
import sys
from typing import List, Dict, Optional
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup

# ---------- Logging ----------
logging.basicConfig(
    level=os.environ.get("LOGLEVEL", "INFO"),
    format="%(levelname)s: %(message)s"
)

# ---------- Constants ----------
SIMPLIFY_README_URL = "https://raw.githubusercontent.com/SimplifyJobs/Summer2026-Internships/dev/README.md"
BOSTON_LOCATIONS = [
    "boston", "cambridge", "somerville", "lexington", "needham", 
    "waltham", "watertown", "brookline", "newton", "burlington",
    "quincy", "norwood", "massachusetts", " ma ", ", ma"
]

# ---------- Models ----------
@dataclass
class JobListing:
    company: str
    title: str
    location: str
    apply_url: str
    date_posted: str
    is_closed: bool = False
    
    def matches_location(self, include_remote: bool = True) -> bool:
        """Check if location matches Boston area or remote."""
        location_lower = self.location.lower()
        
        # Check for remote
        if include_remote and "remote" in location_lower:
            return True
        
        # Check for Boston area locations
        for loc in BOSTON_LOCATIONS:
            if loc in location_lower:
                return True
        
        return False


def fetch_simplify_readme() -> str:
    """Fetch the README.md content from SimplifyJobs repo."""
    try:
        response = requests.get(SIMPLIFY_README_URL, timeout=30)
        response.raise_for_status()
        logging.info(f"Successfully fetched SimplifyJobs README ({len(response.text)} bytes)")
        return response.text
    except requests.RequestException as e:
        logging.error(f"Failed to fetch SimplifyJobs README: {e}")
        raise


def parse_markdown_table(readme_content: str) -> List[JobListing]:
    """
    Parse the HTML tables from SimplifyJobs README.
    
    The README uses markdown headers but HTML tables.
    Extracts jobs from all tech internship sections:
    - Software Engineering
    - Product Management
    - Data Science, AI & Machine Learning
    - Quantitative Finance
    - Hardware Engineering
    """
    jobs = []
    
    # Define all sections we want to scrape
    sections_to_scrape = [
        '💻 Software Engineering Internship Roles',
        '📱 Product Management Internship Roles',
        '🤖 Data Science, AI & Machine Learning Internship Roles',
        '📈 Quantitative Finance Internship Roles',
        '🔧 Hardware Engineering Internship Roles'
    ]
    
    lines = readme_content.split('\n')
    
    for section_name in sections_to_scrape:
        logging.info(f"Parsing section: {section_name}")
        table_html = []
        in_target_section = False
        in_table = False
        
        for line in lines:
            # Look for the target section header
            if f'## {section_name}' in line:
                in_target_section = True
                continue
            
            # Stop at next section (another ## heading that's not our target)
            if in_target_section and line.startswith('## ') and section_name not in line:
                break
            
            # Start collecting table HTML
            if in_target_section and '<table>' in line:
                in_table = True
            
            if in_table:
                table_html.append(line)
            
            # Stop at end of table
            if in_table and '</table>' in line:
                break
        
        if not table_html:
            logging.warning(f"Could not find table in section: {section_name}")
            continue
        
        # Parse the collected HTML table
        table_content = '\n'.join(table_html)
        soup = BeautifulSoup(table_content, 'html.parser')
        table = soup.find('table')
        
        if not table:
            logging.warning(f"Could not parse table HTML for section: {section_name}")
            continue
        
        # Parse all rows in the table body
        rows = table.find_all('tr')
        section_jobs = 0
        
        for row in rows[1:]:  # Skip header row
            cells = row.find_all('td')
            
            if len(cells) < 4:
                continue
            
            try:
                job = parse_html_row(cells)
                if job:
                    jobs.append(job)
                    section_jobs += 1
            except Exception as e:
                logging.debug(f"Error parsing row: {e}")
                continue
        
        logging.info(f"  → Parsed {section_jobs} jobs from {section_name}")
    
    logging.info(f"Parsed {len(jobs)} total job listings from SimplifyJobs (all sections)")
    return jobs


def parse_html_row(cells) -> Optional[JobListing]:
    """Parse HTML table cells into a JobListing."""
    if len(cells) < 4:
        return None
    
    # Get text from each cell
    company_cell = cells[0].get_text(strip=True)
    role_cell = cells[1].get_text(strip=True)
    location_cell = cells[2].get_text(strip=True)
    
    # Check for application link in cell 3
    link_tag = cells[3].find('a')
    apply_url = link_tag['href'] if link_tag and link_tag.get('href') else ""
    
    # Get date from cell 4 if exists
    date_cell = cells[4].get_text(strip=True) if len(cells) > 4 else ""
    
    # Check if position is closed
    is_closed = '🔒' in company_cell or '🔒' in role_cell
    if is_closed:
        return None
    
    # Clean company name
    company_name = extract_company_name(company_cell)
    
    # Clean title
    title = clean_markdown(role_cell)
    
    # Clean and format location
    location = clean_markdown(location_cell)
    location = format_location(location)
    
    # Parse date
    date_posted = parse_date(date_cell)
    
    # Filter out jobs with no relevant locations (format_location returns "" if no relevant locations)
    if not company_name or not title or not location:
        return None
    
    return JobListing(
        company=company_name,
        title=title,
        location=location,
        apply_url=apply_url,
        date_posted=date_posted,
        is_closed=is_closed
    )


def parse_table_row(row: str) -> Optional[JobListing]:
    """Parse a single markdown table row into a JobListing."""
    # Split by | and clean up
    cells = [cell.strip() for cell in row.split('|')]
    
    # Remove empty first/last elements from split
    cells = [c for c in cells if c]
    
    # Need at least 4 columns: Company, Role, Location, Application
    if len(cells) < 4:
        return None
    
    company_cell = cells[0]
    role_cell = cells[1]
    location_cell = cells[2]
    application_cell = cells[3] if len(cells) > 3 else ""
    date_cell = cells[4] if len(cells) > 4 else ""
    
    # Check if position is closed
    is_closed = '🔒' in company_cell or '🔒' in role_cell or 'closed' in application_cell.lower()
    
    if is_closed:
        return None  # Skip closed positions
    
    # Extract company name and URL
    company_name = extract_company_name(company_cell)
    
    # Extract role/title
    title = clean_markdown(role_cell)
    
    # Extract and format location
    location = clean_markdown(location_cell)
    location = format_location(location)
    
    # Extract application URL
    apply_url = extract_url(application_cell)
    if not apply_url:
        # Try to get URL from company cell as fallback
        apply_url = extract_url(company_cell)
    
    # Extract or estimate date
    date_posted = parse_date(date_cell)
    
    if not company_name or not title or not location:
        return None
    
    return JobListing(
        company=company_name,
        title=title,
        location=location,
        apply_url=apply_url or "",
        date_posted=date_posted,
        is_closed=is_closed
    )


def extract_company_name(cell: str) -> str:
    """Extract company name from markdown cell."""
    # Remove emoji indicators
    cell = re.sub(r'[🔥🎓🛂🇺🇸↳]', '', cell)
    
    # Try to extract from [Name](url) format
    match = re.search(r'\[([^\]]+)\]', cell)
    if match:
        return match.group(1).strip()
    
    # Try to extract from **[Name](url)** format
    match = re.search(r'\*\*\[([^\]]+)\]', cell)
    if match:
        return match.group(1).strip()
    
    # Return cleaned cell as fallback
    return clean_markdown(cell)


def extract_url(cell: str) -> str:
    """Extract URL from markdown cell."""
    # Look for href="url" format
    match = re.search(r'href=["\']([^"\']+)["\']', cell)
    if match:
        return match.group(1)
    
    # Look for [text](url) format
    match = re.search(r'\]\(([^)]+)\)', cell)
    if match:
        return match.group(1)
    
    # Look for plain URLs
    match = re.search(r'https?://[^\s<>"]+', cell)
    if match:
        return match.group(0)
    
    return ""


def clean_markdown(text: str) -> str:
    """Remove markdown formatting from text."""
    # Remove bold/italic markers
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    
    # Remove links but keep text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    
    # Remove HTML tags but add space between them
    text = re.sub(r'<[^>]+>', ' ', text)
    
    # Remove emoji and special characters
    text = re.sub(r'[🔥🎓🛂🇺🇸↳]', '', text)
    
    # Clean up whitespace
    text = ' '.join(text.split())
    
    return text.strip()


def is_relevant_location(location: str) -> bool:
    """
    Check if a location is relevant (Boston area or US remote).
    Returns True for Boston area locations and US remote positions.
    Returns False for non-US remote and other locations.
    """
    location_lower = location.lower().strip()
    
    # First, exclude non-US countries explicitly
    non_us_patterns = [
        ', uk', ' uk', ',uk', 'united kingdom',
        ', canada', ' canada',
        ', india', ' india',
        ', mexico', ' mexico',
        ', europe', ' europe',
        ', australia', ' australia',
        ', brazil', ' brazil',
        ', israel', ' israel',
        ', china', ' china',
        ', japan', ' japan',
        ', singapore', ' singapore',
        ', germany', ' germany',
        ', france', ' france',
        ', netherlands', ' netherlands',
        ', spain', ' spain',
        ', italy', ' italy',
        'remote in uk', 'remote in canada', 'remote in india', 'remote in mexico',
        'remote in europe', 'remote in australia', 'remote in brazil', 'remote in israel',
        'remote in china', 'remote in japan', 'remote in singapore', 'remote in germany',
        'remote in france', 'remote in netherlands', 'remote in spain', 'remote in italy'
    ]
    
    for pattern in non_us_patterns:
        if pattern in location_lower:
            return False
    
    # Check for Boston area locations
    for loc in BOSTON_LOCATIONS:
        if loc in location_lower:
            return True
    
    # Check for Remote (generic) or Remote in USA
    if location_lower == 'remote' or 'remote in usa' in location_lower or 'remote in us' in location_lower:
        return True
    
    # Check for Remote (no location) or US-specific remote
    if location_lower.startswith('remote') and 'in' not in location_lower:
        return True
    
    return False


def format_location(location: str) -> str:
    """Format location string with proper separators, filtering, and truncation."""
    if not location:
        return location
    
    # Protect certain patterns from being split (use lowercase placeholders to avoid regex matches)
    location = location.replace('Remote in USA', '___remote_usa___')
    location = location.replace('Remote in UK', '___remote_uk___')
    location = location.replace('Remote in Canada', '___remote_canada___')
    location = location.replace('Remote in India', '___remote_india___')
    location = location.replace('Remote in Europe', '___remote_europe___')
    
    # Add commas between locations that are missing them
    # Pattern: matches state abbreviation followed by capital letter (new location)
    # Handle patterns like "MA" + "New York" or "MA" + "NYC" 
    location = re.sub(r'([A-Z]{2})([A-Z]{2,}[a-z])', r'\1, \2', location)  # MA + NewYork
    location = re.sub(r'([A-Z]{2})([A-Z]{3,})', r'\1, \2', location)  # MA + NYC
    location = re.sub(r'([A-Z]{2})([A-Z][a-z])', r'\1, \2', location)  # MA + Washington
    
    # Add commas between city, state and another city (lowercase to uppercase transition)
    location = re.sub(r'([a-z])([A-Z][a-z])', r'\1, \2', location)
    
    # Add commas between "Remote in X" patterns
    location = re.sub(r'(Remote in [A-Z]{2,})([A-Z])', r'\1, \2', location)
    location = re.sub(r'(Remote in [A-Za-z\s]+?)([A-Z][a-z]+, [A-Z]{2})', r'\1, \2', location)
    
    # Handle "X locations" pattern at the start
    location = re.sub(r'(\d+ locations)([A-Z])', r'\1, \2', location)
    
    # Restore protected patterns
    location = location.replace('___remote_usa___', 'Remote in USA')
    location = location.replace('___remote_uk___', 'Remote in UK')
    location = location.replace('___remote_canada___', 'Remote in Canada')
    location = location.replace('___remote_india___', 'Remote in India')
    location = location.replace('___remote_europe___', 'Remote in Europe')
    
    # Split by common delimiters (semicolon or comma)
    locations = re.split(r'[;]|,(?!\s*[A-Z]{2}\s*$)', location)  # Split by semicolon or comma, but not before a state code
    locations = [loc.strip() for loc in locations if loc.strip()]
    
    # Merge city with state if they got split (e.g., "Boston" and "MA" -> "Boston, MA")
    merged_locations = []
    i = 0
    while i < len(locations):
        current = locations[i]
        # Check if next item is a 2-letter state code
        if i + 1 < len(locations) and re.match(r'^[A-Z]{2}$', locations[i + 1].strip()):
            # Merge them
            merged_locations.append(f"{current}, {locations[i + 1]}")
            i += 2
        else:
            merged_locations.append(current)
            i += 1
    
    locations = merged_locations
    
    # Filter to only relevant locations (Boston area or US remote)
    filtered_locations = []
    for loc in locations:
        if is_relevant_location(loc):
            filtered_locations.append(loc)
    locations = filtered_locations
    
    # If no relevant locations remain, return empty (job will be filtered out)
    if not locations:
        return ""
    
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
        # Take first 2-3 locations that fit reasonably
        kept_locations = []
        total_length = 0
        
        for loc in locations[:3]:  # Max 3 locations shown
            if total_length + len(loc) > 50 and kept_locations:
                break
            kept_locations.append(loc)
            total_length += len(loc) + 2  # +2 for ", "
        
        result = ', '.join(kept_locations)
        
        # If we truncated, show count
        if len(locations) > len(kept_locations):
            remaining = len(locations) - len(kept_locations)
            result += f'<br>+{remaining} more'
        
        return result
    
    return ', '.join(locations)


def parse_date(date_cell: str) -> str:
    """
    Parse date from cell. Returns formatted date or 'N/A'.
    SimplifyJobs uses format like 'Oct 17', '2d', '1w', etc.
    """
    if not date_cell or date_cell.strip() == '':
        return "N/A"
    
    date_str = clean_markdown(date_cell).strip()
    
    # If it's already a date-like format (e.g., "Oct 17"), try to add current year
    try:
        # Try to parse formats like "Oct 17", "10/17", etc.
        for fmt in ["%b %d", "%m/%d", "%B %d"]:
            try:
                parsed = dt.datetime.strptime(date_str, fmt)
                # Add current year
                current_year = dt.datetime.now().year
                full_date = parsed.replace(year=current_year)
                return full_date.strftime("%m/%d/%Y")
            except ValueError:
                continue
    except:
        pass
    
    # Handle relative dates (e.g., "2d", "1w")
    match = re.match(r'(\d+)([dDwWhHmM])', date_str)
    if match:
        num = int(match.group(1))
        unit = match.group(2).lower()
        
        today = dt.datetime.now()
        if unit == 'd':
            estimated_date = today - dt.timedelta(days=num)
        elif unit == 'w':
            estimated_date = today - dt.timedelta(weeks=num)
        elif unit == 'h':
            estimated_date = today - dt.timedelta(hours=num)
        elif unit == 'm':
            estimated_date = today - dt.timedelta(days=num * 30)  # Approximate
        else:
            return "N/A"
        
        return estimated_date.strftime("%m/%d/%Y")
    
    # If we can't parse it, return as-is or N/A
    return date_str if date_str else "N/A"


def parse_date_to_datetime(date_str: str) -> dt.datetime:
    """
    Convert a date string to datetime object for sorting.
    Returns a datetime object, defaulting to very old date if can't parse.
    """
    if not date_str or date_str == "N/A":
        # Return very old date so N/A dates go to bottom
        return dt.datetime(1900, 1, 1)
    
    try:
        # Try parsing MM/DD/YYYY format
        return dt.datetime.strptime(date_str, "%m/%d/%Y")
    except ValueError:
        pass
    
    try:
        # Try parsing M/D/YYYY format
        return dt.datetime.strptime(date_str, "%m/%d/%Y")
    except ValueError:
        pass
    
    # If we can't parse, return old date
    return dt.datetime(1900, 1, 1)


def filter_boston_remote(jobs: List[JobListing], include_remote: bool = True) -> List[JobListing]:
    """Filter jobs for Boston area and optionally remote positions."""
    filtered = [job for job in jobs if job.matches_location(include_remote)]
    logging.info(f"Filtered to {len(filtered)} Boston/Remote positions")
    return filtered


def format_for_readme(jobs: List[JobListing]) -> str:
    """Format job listings for README table."""
    if not jobs:
        return ""
    
    rows = []
    for job in jobs:
        # Format the apply link
        apply_link = f"[APPLY]({job.apply_url})" if job.apply_url else "N/A"
        
        row = f"| {job.company} | {job.title} | {job.location} | {job.date_posted} | {apply_link} |"
        rows.append(row)
    
    return '\n'.join(rows)


def get_existing_jobs() -> set:
    """Get set of existing job identifiers from README to avoid duplicates."""
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    
    if not os.path.exists(readme_path):
        return set()
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract job identifiers (company + title as simple check)
        existing = set()
        for line in content.split('\n'):
            if line.startswith('|') and '|' in line[1:]:
                cells = [c.strip() for c in line.split('|')]
                if len(cells) >= 3:
                    # Use company + title as identifier
                    company = clean_markdown(cells[1])
                    title = clean_markdown(cells[2])
                    if company and title:
                        existing.add(f"{company}|{title}".lower())
        
        logging.info(f"Found {len(existing)} existing jobs in README")
        return existing
    except Exception as e:
        logging.warning(f"Could not read existing README: {e}")
        return set()


def deduplicate_jobs(jobs: List[JobListing], existing: set) -> List[JobListing]:
    """Remove jobs that already exist in README."""
    new_jobs = []
    for job in jobs:
        identifier = f"{job.company}|{job.title}".lower()
        if identifier not in existing:
            new_jobs.append(job)
    
    logging.info(f"After deduplication: {len(new_jobs)} new jobs")
    return new_jobs


def append_to_readme(jobs: List[JobListing]) -> None:
    """Append new jobs to README.md."""
    if not jobs:
        logging.info("No new jobs to add to README")
        return
    
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    
    try:
        # Read existing content
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the job listings table
        # Look for the line with the table header
        table_pattern = r'(\| Company Name \| Job Title \| Location \| Date Posted \| APPLY \|)'
        match = re.search(table_pattern, content)
        
        if not match:
            logging.error("Could not find job listings table in README")
            return
        
        # Find the end of the header (separator line)
        header_end = content.find('\n', match.end())
        separator_end = content.find('\n', header_end + 1)
        
        # Format new jobs
        new_jobs_text = format_for_readme(jobs)
        
        # Insert after the separator line
        new_content = (
            content[:separator_end + 1] +
            new_jobs_text + '\n' +
            content[separator_end + 1:]
        )
        
        # Write back
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        logging.info(f"✅ Added {len(jobs)} new jobs to README.md")
        
        # Print summary
        print(f"\n{'='*60}")
        print(f"Added {len(jobs)} new jobs from SimplifyJobs:")
        print(f"{'='*60}")
        for job in jobs:
            print(f"  • {job.company} - {job.title}")
            print(f"    📍 {job.location}")
        print(f"{'='*60}\n")
        
    except Exception as e:
        logging.error(f"Failed to append to README: {e}")
        raise


def main():
    ap = argparse.ArgumentParser(
        description="Scrape SimplifyJobs Summer2026-Internships for Boston area jobs"
    )
    ap.add_argument("--no-remote", action="store_true", 
                    help="Exclude remote positions")
    ap.add_argument("--dry-run", action="store_true",
                    help="Show what would be added without modifying README")
    args = ap.parse_args()
    
    print("🔍 Fetching jobs from SimplifyJobs/Summer2026-Internships...")
    
    # Fetch and parse
    readme_content = fetch_simplify_readme()
    all_jobs = parse_markdown_table(readme_content)
    
    # Filter for Boston/Remote
    include_remote = not args.no_remote
    filtered_jobs = filter_boston_remote(all_jobs, include_remote)
    
    if not filtered_jobs:
        print("No Boston/Remote jobs found in SimplifyJobs repo")
        return
    
    # Deduplicate
    existing_jobs = get_existing_jobs()
    new_jobs = deduplicate_jobs(filtered_jobs, existing_jobs)
    
    if not new_jobs:
        print("✨ No new jobs to add - all SimplifyJobs listings are already in your README!")
        return
    
    # Sort by date (newest first)
    new_jobs.sort(key=lambda j: parse_date_to_datetime(j.date_posted), reverse=True)
    
    # Show preview
    print(f"\n📋 Found {len(new_jobs)} new jobs:")
    for job in new_jobs[:10]:  # Show first 10
        print(f"  • {job.company} - {job.title} ({job.location})")
    if len(new_jobs) > 10:
        print(f"  ... and {len(new_jobs) - 10} more")
    
    if args.dry_run:
        print("\n[DRY RUN] Would have added these jobs to README.md")
        return
    
    # Append to README
    append_to_readme(new_jobs)


if __name__ == "__main__":
    main()
