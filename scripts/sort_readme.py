#!/usr/bin/env python3
"""
Sort jobs in README.md by date (newest first).
"""

import re
import os
from datetime import datetime
from typing import List, Tuple


def parse_date_to_datetime(date_str: str) -> datetime:
    """Convert date string to datetime for sorting."""
    if not date_str or date_str == "N/A":
        return datetime(1900, 1, 1)
    
    try:
        return datetime.strptime(date_str, "%m/%d/%Y")
    except ValueError:
        pass
    
    try:
        return datetime.strptime(date_str, "%m/%d/%Y")
    except ValueError:
        pass
    
    return datetime(1900, 1, 1)


def extract_jobs_from_readme() -> Tuple[str, List[Tuple[str, datetime]], str]:
    """
    Extract job rows from README and parse their dates.
    Returns: (header_section, list of (row, date), footer_section)
    """
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the table
    table_header_pattern = r'\| Company Name \| Job Title \| Location \| Date Posted \| APPLY \|'
    match = re.search(table_header_pattern, content)
    
    if not match:
        raise ValueError("Could not find job table in README")
    
    # Find header end (after separator line)
    header_end = content.find('\n', match.end())
    separator_end = content.find('\n', header_end + 1)
    
    # Find the end of the table (next ---) 
    table_end = content.find('\n---', separator_end)
    if table_end == -1:
        # If no ---, find next ## heading
        table_end = content.find('\n## ', separator_end)
    
    if table_end == -1:
        raise ValueError("Could not find end of job table")
    
    # Extract sections
    header_section = content[:separator_end + 1]
    table_rows_text = content[separator_end + 1:table_end]
    footer_section = content[table_end:]
    
    # Parse each row
    jobs_with_dates = []
    for line in table_rows_text.strip().split('\n'):
        line = line.strip()
        if not line or not line.startswith('|'):
            continue
        
        # Extract date from row (4th column)
        cells = [c.strip() for c in line.split('|')]
        cells = [c for c in cells if c]  # Remove empty
        
        if len(cells) >= 4:
            date_str = cells[3]  # Date Posted column
            date_obj = parse_date_to_datetime(date_str)
            jobs_with_dates.append((line, date_obj))
    
    return header_section, jobs_with_dates, footer_section


def sort_and_write_readme():
    """Sort README jobs by date and rewrite file."""
    print("📊 Sorting README.md by date (newest first)...")
    
    header, jobs_with_dates, footer = extract_jobs_from_readme()
    
    print(f"Found {len(jobs_with_dates)} jobs to sort")
    
    # Sort by date (newest first)
    jobs_with_dates.sort(key=lambda x: x[1], reverse=True)
    
    # Reconstruct content
    sorted_rows = [row for row, date in jobs_with_dates]
    new_content = header + '\n'.join(sorted_rows) + '\n' + footer
    
    # Write back
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Sorted {len(jobs_with_dates)} jobs by date")
    print(f"   Newest: {jobs_with_dates[0][1].strftime('%m/%d/%Y') if jobs_with_dates else 'N/A'}")
    print(f"   Oldest: {jobs_with_dates[-1][1].strftime('%m/%d/%Y') if jobs_with_dates else 'N/A'}")


if __name__ == "__main__":
    sort_and_write_readme()
