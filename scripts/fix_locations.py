#!/usr/bin/env python3
"""
Fix malformed location strings in README.md
"""

import re
import os

def format_location(location: str) -> str:
    """Format location string with proper separators and truncation."""
    if not location:
        return location
    
    # Protect certain patterns from being split
    location = location.replace('Remote in USA', '<<<REMOTE_USA>>>')
    location = location.replace('Remote in Canada', '<<<REMOTE_CANADA>>>')
    location = location.replace('Remote in UK', '<<<REMOTE_UK>>>')
    
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
    location = location.replace('<<<REMOTE_UK>>>', 'Remote in UK')
    
    # Split by commas and clean up
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
    
    # If too many locations or too long, truncate
    if len(locations) > 3 or len(', '.join(locations)) > 60:
        kept_locations = []
        total_length = 0
        
        for loc in locations[:3]:
            if total_length + len(loc) > 60 and kept_locations:
                break
            kept_locations.append(loc)
            total_length += len(loc) + 2
        
        result = ', '.join(kept_locations)
        
        if len(locations) > len(kept_locations):
            remaining = len(locations) - len(kept_locations)
            result += f' (+{remaining} more)'
        
        return result
    
    return ', '.join(locations)


def fix_readme_locations():
    """Fix all malformed locations in README.md"""
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the job table
    lines = content.split('\n')
    fixed_lines = []
    changes_made = 0
    
    for line in lines:
        # Check if this is a table row (has pipes)
        if line.startswith('|') and line.count('|') >= 5:
            # Split the line by pipes
            parts = line.split('|')
            
            # Job table has format: | Company | Title | Location | Date | Apply |
            if len(parts) >= 6:
                location = parts[3].strip()
                
                # Check if location looks malformed (very long without commas)
                if len(location) > 60 and ',' not in location[:50]:
                    # Fix the location
                    fixed_location = format_location(location)
                    parts[3] = f' {fixed_location} '
                    fixed_line = '|'.join(parts)
                    fixed_lines.append(fixed_line)
                    changes_made += 1
                    print(f"Fixed: {location[:80]}... -> {fixed_location}")
                    continue
        
        # Keep line as-is
        fixed_lines.append(line)
    
    # Write back
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(fixed_lines))
    
    print(f"\n✅ Fixed {changes_made} location entries in README.md")


if __name__ == '__main__':
    fix_readme_locations()
