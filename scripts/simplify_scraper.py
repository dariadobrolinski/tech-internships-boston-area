#!/usr/bin/env python3
"""
GitHub Internship Scraper
Fetches tech internship listings from multiple GitHub repos and filters
for Boston area and remote positions.

Sources:
- SimplifyJobs/Summer2026-Internships
- speedyapply/2026-SWE-College-Jobs
- vanshb03/Summer2026-Internships

Usage:
    python simplify_scraper.py --out ./reports
"""

import argparse
import datetime as dt
import logging
import os
import re
import sys
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup

# ---------- Logging ----------
logging.basicConfig(
    level=os.environ.get("LOGLEVEL", "INFO"),
    format="%(levelname)s: %(message)s"
)

# ---------- Constants ----------
# GitHub repo sources (URL, branch, owner credit)
GITHUB_SOURCES = [
    {
        "name": "SimplifyJobs",
        "url": "https://raw.githubusercontent.com/SimplifyJobs/Summer2026-Internships/dev/README.md",
        "owner": "SimplifyJobs",
        "repo": "Summer2026-Internships"
    },
    {
        "name": "SpeedyApply",
        "url": "https://raw.githubusercontent.com/speedyapply/2026-SWE-College-Jobs/main/README.md",
        "owner": "speedyapply",
        "repo": "2026-SWE-College-Jobs"
    },
    {
        "name": "vanshb03",
        "url": "https://raw.githubusercontent.com/vanshb03/Summer2026-Internships/main/README.md",
        "owner": "vanshb03",
        "repo": "Summer2026-Internships"
    }
]

# Boston area cities that are unambiguous (only in MA)
BOSTON_LOCATIONS_UNAMBIGUOUS = [
    "boston", "cambridge", "somerville", "lexington", "needham", 
    "waltham", "watertown", "brookline", "quincy", "norwood",
    "framingham", "lowell", "worcester", "andover",
    "marlborough", "peabody", "dedham", "acton", "bedford",
    "pittsfield", "fall river", "attleboro", "westborough",
    "massachusetts", " ma ", ", ma"
]

# Cities that exist in multiple states - require MA/Massachusetts to match
BOSTON_LOCATIONS_AMBIGUOUS = [
    "newton",      # Newton, MA vs Newton, IA
    "burlington",  # Burlington, MA vs Burlington, VT
    "lawrence"     # Lawrence, MA vs Lawrence, KS
]

# ---------- Models ----------
@dataclass
class JobListing:
    company: str
    title: str
    location: str
    apply_url: str
    date_posted: str
    source: str = ""  # Which GitHub repo this came from
    is_closed: bool = False
    
    def matches_location(self, include_remote: bool = True) -> bool:
        """Check if location matches Boston area or remote."""
        # Use the same logic as is_relevant_location function
        location_lower = self.location.lower()
        
        # Exclude other US states explicitly (not MA)
        non_ma_states = [
            ', ks', ', kansas', ', az', ', arizona', ', co', ', colorado',
            ', vt', ', vermont', ', ia', ', iowa', ', ny', ', new york',
            ', ca', ', california', ', tx', ', texas', ', fl', ', florida',
            ', wa', ', washington', 'denver, colorado', 'tempe, az'
        ]
        for pattern in non_ma_states:
            if pattern in location_lower:
                return False
        
        # Check for remote
        if include_remote and "remote" in location_lower:
            # Make sure it's US remote, not international
            if "remote in usa" in location_lower or "remote in us" in location_lower:
                return True
            if location_lower == "remote":
                return True
            if location_lower.startswith('remote') and 'in' not in location_lower:
                return True
            # If it says "remote in <country>", check if it's filtered out
            non_us_remote = ['remote in uk', 'remote in canada', 'remote in india', 
                           'remote in europe', 'remote in mexico']
            for pattern in non_us_remote:
                if pattern in location_lower:
                    return False
        
        # Check for unambiguous Boston area locations
        for loc in BOSTON_LOCATIONS_UNAMBIGUOUS:
            if loc in location_lower:
                return True
        
        # Check for ambiguous city names - require MA/Massachusetts
        for city in BOSTON_LOCATIONS_AMBIGUOUS:
            if city in location_lower:
                # Only accept if it also contains MA or Massachusetts
                if ', ma' in location_lower or ' ma' in location_lower or 'massachusetts' in location_lower:
                    return True
                # Otherwise reject
                return False
        
        return False


def fetch_readme(url: str, source_name: str) -> str:
    """Fetch README.md content from a GitHub repo."""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        logging.info(f"Successfully fetched {source_name} README ({len(response.text)} bytes)")
        return response.text
    except requests.RequestException as e:
        logging.error(f"Failed to fetch {source_name} README: {e}")
        return ""


def parse_markdown_table(readme_content: str, source_name: str = "") -> List[JobListing]:
    """
    Parse tables from GitHub README files (both HTML and markdown formats).
    
    Extracts jobs from internship listings, filtering for tech roles.
    Excludes Product Management positions.
    """
    jobs = []
    
    # Try HTML table format first (SimplifyJobs style)
    html_jobs = parse_html_tables(readme_content, source_name)
    if html_jobs:
        return html_jobs
    
    # Fall back to markdown table format (speedyapply, vanshb03 style)
    md_jobs = parse_plain_markdown_tables(readme_content, source_name)
    return md_jobs


def parse_html_tables(readme_content: str, source_name: str = "") -> List[JobListing]:
    """Parse HTML tables (SimplifyJobs format)."""
    jobs = []
    
    # Define all sections we want to scrape
    sections_to_scrape = [
        '💻 Software Engineering Internship Roles',
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
                job = parse_html_row(cells, source_name)
                if job:
                    jobs.append(job)
                    section_jobs += 1
            except Exception as e:
                logging.debug(f"Error parsing row: {e}")
                continue
        
        logging.info(f"  → Parsed {section_jobs} jobs from {section_name}")
    
    logging.info(f"Parsed {len(jobs)} total job listings from {source_name} (all sections)")
    return jobs


def parse_plain_markdown_tables(readme_content: str, source_name: str = "") -> List[JobListing]:
    """Parse plain markdown tables (speedyapply, vanshb03 format)."""
    jobs = []
    lines = readme_content.split('\n')
    
    in_table = False
    table_started = False
    
    for i, line in enumerate(lines):
        # Look for table separator (|---|---|)
        if '|' in line and ('---' in line or '===' in line):
            in_table = True
            table_started = True
            continue
        
        # If we were in a table and hit an empty line or non-table line, stop
        if table_started and (not line.strip() or (line.strip() and '|' not in line)):
            in_table = False
            continue
        
        # Parse table rows
        if in_table and '|' in line and line.strip().startswith('|'):
            try:
                job = parse_markdown_row(line, source_name)
                if job:
                    jobs.append(job)
            except Exception as e:
                logging.debug(f"Error parsing markdown row: {e}")
                continue
    
    logging.info(f"Parsed {len(jobs)} total job listings from {source_name}")
    return jobs


def parse_markdown_row(row: str, source_name: str = "") -> Optional[JobListing]:
    """Parse a markdown table row."""
    # Split by | and clean up
    cells = [cell.strip() for cell in row.split('|')]
    cells = [c for c in cells if c]  # Remove empty cells
    
    if len(cells) < 3:
        return None
    
    # Extract data (format: Company | Position | Location | ... )
    company_cell = cells[0]
    position_cell = cells[1]
    location_cell = cells[2]
    
    # Get URL from any cell (usually in position or company)
    apply_url = extract_url(company_cell) or extract_url(position_cell)
    if len(cells) > 3:
        apply_url = apply_url or extract_url(cells[3])
    
    # Get date if available (usually last column or in "Age" column)
    date_cell = cells[-1] if len(cells) > 4 else ""
    
    # Check for closed/filled indicators
    if '🔒' in row or 'closed' in row.lower() or 'filled' in row.lower():
        return None
    
    # Clean company name
    company_name = extract_company_name(company_cell)
    if not company_name:
        return None
    
    # Clean title
    title = clean_markdown(position_cell)
    if not title:
        return None
    
    # Filter out Product Manager positions
    title_lower = title.lower()
    if 'product manager' in title_lower or 'product management' in title_lower:
        if 'software' not in title_lower and 'engineer' not in title_lower:
            return None
    
    # Clean and format location
    location = clean_markdown(location_cell)
    location = format_location(location)
    
    # Filter out jobs with no relevant locations
    if not location:
        return None
    
    # Parse date
    date_posted = parse_date(date_cell)
    
    return JobListing(
        company=company_name,
        title=title,
        location=location,
        apply_url=apply_url or "",
        date_posted=date_posted,
        source=source_name,
        is_closed=False
    )


def parse_html_row(cells, source_name: str = "") -> Optional[JobListing]:
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
        source=source_name,
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
    
    # Exclude other US states explicitly (not MA)
    non_ma_states = [
        ', ks', ', kansas',  # Lawrence, KS
        ', az', ', arizona',  # Tempe, AZ
        ', co', ', colorado',  # Denver, CO
        ', vt', ', vermont',  # Burlington, VT
        ', ia', ', iowa',  # Newton, IA
        ', ny', ', new york',
        ', ca', ', california',
        ', tx', ', texas',
        ', fl', ', florida',
        ', wa', ', washington',
        ', or', ', oregon',
        ', il', ', illinois',
        ', pa', ', pennsylvania',
        ', oh', ', ohio',
        ', nc', ', north carolina',
        ', ga', ', georgia',
        ', mi', ', michigan',
        ', nj', ', new jersey',
        ', va', ', virginia',
        ', ct', ', connecticut',
        ', ri', ', rhode island',
        ', nh', ', new hampshire',
        ', me', ', maine',
        'denver, colorado',
        'tempe, az'
    ]
    
    for pattern in non_ma_states:
        if pattern in location_lower:
            return False
    
    # Check for unambiguous Boston area locations (only exist in MA)
    for loc in BOSTON_LOCATIONS_UNAMBIGUOUS:
        if loc in location_lower:
            return True
    
    # Check for ambiguous city names - require MA/Massachusetts in the location string
    for city in BOSTON_LOCATIONS_AMBIGUOUS:
        if city in location_lower:
            # Only accept if it also contains MA or Massachusetts
            if ', ma' in location_lower or ' ma' in location_lower or 'massachusetts' in location_lower:
                return True
            # Otherwise reject (e.g., "Newton, IA" or "Burlington, VT")
            return False
    
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
    
    # Add commas/separators between locations that are missing them
    # Handle edge cases like "CT Norwood, MA" (two separate locations concatenated)
    
    # Pattern 1: "STATE City, STATE" -> "STATE; City, STATE"
    # e.g., "CT Norwood, MA" -> "CT; Norwood, MA"
    location = re.sub(r'\b([A-Z]{2})\s+([A-Z][a-z]+),\s*([A-Z]{2})\b', r'\1; \2, \3', location)
    
    # Pattern 2: "City, STATE City, STATE" -> "City, STATE; City, STATE"
    # e.g., "Boston, MA Cambridge, MA" -> "Boston, MA; Cambridge, MA"
    location = re.sub(r'([a-z], [A-Z]{2})\s+([A-Z][a-z]+)', r'\1; \2', location)
    
    # Handle "X locations" pattern at the start
    location = re.sub(r'(\d+ locations)([A-Z])', r'\1, \2', location)
    
    # Add commas between "Remote in X" patterns and other locations
    location = re.sub(r'(Remote in [A-Z]{2,})([A-Z])', r'\1; \2', location)
    location = re.sub(r'(Remote in [A-Za-z\s]+?)([A-Z][a-z]+, [A-Z]{2})', r'\1; \2', location)
    
    # Restore protected patterns
    location = location.replace('___remote_usa___', 'Remote in USA')
    location = location.replace('___remote_uk___', 'Remote in UK')
    location = location.replace('___remote_canada___', 'Remote in Canada')
    location = location.replace('___remote_india___', 'Remote in India')
    location = location.replace('___remote_europe___', 'Remote in Europe')
    
    # Split by semicolons primarily (indicates separate locations)
    # Also split by commas but be careful not to split city, state pairs
    locations = re.split(r';', location)  # Split by semicolon first
    
    # Now handle comma-separated locations within each segment
    expanded_locations = []
    for segment in locations:
        # Only split by comma if it's not part of a "City, ST" pattern
        # Look for pattern: word, 2-letter-code and keep it together
        if re.search(r'[a-zA-Z]+,\s*[A-Z]{2}(?:\s|$)', segment):
            # Has city, state pattern - keep as is
            expanded_locations.append(segment.strip())
        else:
            # No state pattern, can split by commas
            parts = [p.strip() for p in segment.split(',')]
            expanded_locations.extend([p for p in parts if p])
    
    locations = [loc.strip() for loc in expanded_locations if loc.strip()]
    
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
    
    # Format locations - show all relevant ones
    # If there are many, just show them all in a compact format
    if len(locations) > 4:
        # Show first location prominently, then list count of others
        # E.g., "Boston, MA (+3 other locations)"
        result = f"{locations[0]} (+{len(locations)-1} other location{'s' if len(locations) > 2 else ''})"
        return result
    elif len(locations) > 1:
        # For 2-4 locations, show them all but compactly
        # Use semicolons to save space
        return '; '.join(locations)
    else:
        # Single location - just return it
        return locations[0] if locations else ""


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
        apply_link = f'[APPLY]({job.apply_url})' if job.apply_url else "N/A"
        
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


def deduplicate_across_sources(jobs: List[JobListing]) -> List[JobListing]:
    """
    Remove duplicate jobs across multiple sources.
    Keeps the first occurrence (prioritizes earlier sources).
    """
    seen = set()
    unique_jobs = []
    duplicates_removed = 0
    
    for job in jobs:
        # Create identifier from company + title (case-insensitive)
        identifier = f"{job.company}|{job.title}".lower()
        
        if identifier not in seen:
            seen.add(identifier)
            unique_jobs.append(job)
        else:
            duplicates_removed += 1
            logging.debug(f"Skipping duplicate: {job.company} - {job.title} (from {job.source})")
    
    if duplicates_removed > 0:
        logging.info(f"Removed {duplicates_removed} duplicates across sources")
    
    return unique_jobs


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
        
        # Print summary grouped by source
        print(f"\n{'='*60}")
        print(f"✅ Added {len(jobs)} new jobs to README.md")
        print(f"{'='*60}")
        
        # Group by source
        by_source = {}
        for job in jobs:
            if job.source not in by_source:
                by_source[job.source] = []
            by_source[job.source].append(job)
        
        for source_name, source_jobs in by_source.items():
            print(f"\n📦 From {source_name} ({len(source_jobs)} jobs):")
            for job in source_jobs[:5]:  # Show first 5 from each source
                print(f"  • {job.company} - {job.title}")
                print(f"    📍 {job.location}")
            if len(source_jobs) > 5:
                print(f"  ... and {len(source_jobs) - 5} more")
        
        print(f"\n{'='*60}\n")
        
    except Exception as e:
        logging.error(f"Failed to append to README: {e}")
        raise


def main():
    ap = argparse.ArgumentParser(
        description="Scrape multiple GitHub repos for Summer 2026 internships in Boston area"
    )
    ap.add_argument("--no-remote", action="store_true", 
                    help="Exclude remote positions")
    ap.add_argument("--dry-run", action="store_true",
                    help="Show what would be added without modifying README")
    args = ap.parse_args()
    
    print("🔍 Fetching jobs from multiple GitHub repositories...")
    print(f"   Sources: {', '.join([s['owner'] + '/' + s['repo'] for s in GITHUB_SOURCES])}")
    print()
    
    all_jobs = []
    
    # Fetch and parse from all sources
    for source in GITHUB_SOURCES:
        print(f"📥 Fetching from {source['owner']}/{source['repo']}...")
        readme_content = fetch_readme(source['url'], source['name'])
        
        if readme_content:
            jobs = parse_markdown_table(readme_content, source['name'])
            all_jobs.extend(jobs)
            print(f"   ✓ Found {len(jobs)} jobs from {source['name']}")
        else:
            print(f"   ⚠️  Could not fetch from {source['name']}")
        print()
    
    if not all_jobs:
        print("❌ No jobs found from any source")
        return
    
    print(f"📊 Total jobs fetched: {len(all_jobs)}")
    
    # Deduplicate across sources first (before filtering)
    all_jobs = deduplicate_across_sources(all_jobs)
    print(f"📊 After cross-source deduplication: {len(all_jobs)} unique jobs")
    
    # Filter for Boston/Remote
    include_remote = not args.no_remote
    filtered_jobs = filter_boston_remote(all_jobs, include_remote)
    
    if not filtered_jobs:
        print("No Boston/Remote jobs found")
        return
    
    # Deduplicate against existing README jobs
    existing_jobs = get_existing_jobs()
    new_jobs = deduplicate_jobs(filtered_jobs, existing_jobs)
    
    if not new_jobs:
        print("✨ No new jobs to add - all listings are already in your README!")
        return
    
    # Sort by date (newest first)
    new_jobs.sort(key=lambda j: parse_date_to_datetime(j.date_posted), reverse=True)
    
    # Show preview grouped by source
    print(f"\n📋 Found {len(new_jobs)} new jobs:")
    source_counts = {}
    for job in new_jobs:
        source_counts[job.source] = source_counts.get(job.source, 0) + 1
    
    for source_name, count in source_counts.items():
        print(f"   • {source_name}: {count} jobs")
    
    print("\nPreview (first 10):")
    for job in new_jobs[:10]:
        print(f"  • {job.company} - {job.title}")
        print(f"    📍 {job.location} | 📅 {job.date_posted} | 🔗 {job.source}")
    if len(new_jobs) > 10:
        print(f"  ... and {len(new_jobs) - 10} more")
    
    if args.dry_run:
        print("\n[DRY RUN] Would have added these jobs to README.md")
        return
    
    # Append to README
    append_to_readme(new_jobs)
    
    # Print credits
    print("\n" + "="*60)
    print("📚 Data sources - Thank you to:")
    for source in GITHUB_SOURCES:
        print(f"   • {source['owner']}/{source['repo']}")
    print("="*60)


if __name__ == "__main__":
    main()
