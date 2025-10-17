# Contributing to Boston Tech Internship Finder

Thank you for your interest in contributing! This project helps students find tech internships in the Boston area.

## How to Contribute

### 1. Adding New Companies

The easiest way to contribute is by adding companies to `config/companies.yml`:

```yaml
companies:
  - name: CompanyName
    provider: greenhouse  # or "lever"
    slug: company-slug
    include_keywords: []  # Optional: add specific keywords to include
    exclude_keywords: []  # Optional: add keywords to exclude
```

**How to find company slugs:**
- **Greenhouse**: Visit `https://boards.greenhouse.io/COMPANY-NAME` and check if it loads
- **Lever**: Visit `https://jobs.lever.co/COMPANY-NAME` and check if it loads

### 2. Improving Search Keywords

Edit the keyword filters in `scripts/job_report.py`:
- **Include keywords**: Add terms that internships should contain
- **Exclude keywords**: Add seniority terms to filter out (senior, staff, etc.)

### 3. Adding New Job Boards

To add support for a new job board API:
1. Create a new script in `scripts/` (e.g., `new_board_report.py`)
2. Follow the pattern in `job_report.py`:
   - Fetch jobs from the API
   - Normalize the data format
   - Check for duplicates before adding to README
   - Use regex to extract existing URLs from README
3. Add the script to `run_all.sh`

### 4. Bug Fixes & Features

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test thoroughly**
   ```bash
   ./run_all.sh
   ```
5. **Commit with clear messages**
   ```bash
   git commit -m "Add feature: description of what you added"
   ```
6. **Push and create a Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Style Guidelines

### Python
- Use clear variable names
- Add docstrings to functions
- Follow PEP 8 style guide
- Handle errors gracefully with try/except

### Example
```python
def fetch_jobs(company_slug: str) -> List[Dict[str, Any]]:
    """
    Fetch jobs from the API for a given company.
    
    Args:
        company_slug: The company's slug identifier
        
    Returns:
        List of job dictionaries
    """
    try:
        # Your code here
        pass
    except Exception as e:
        logging.warning(f"Failed to fetch jobs: {e}")
        return []
```

## Testing Your Changes

Before submitting a PR:

1. **Test the main script**
   ```bash
   ./run_all.sh
   ```

2. **Check that duplicates are handled**
   - Run the script twice
   - Verify no duplicate jobs appear in README

3. **Verify README format**
   - Check the table is properly formatted
   - Ensure all links work

4. **Test with different configurations**
   - Try with/without API keys
   - Test with `--include-remote` flag

## Pull Request Guidelines

### Good PR Title Examples
- ✅ `Add 15 new Boston tech companies`
- ✅ `Fix duplicate detection for Adzuna jobs`
- ✅ `Add support for Indeed API`

### Bad PR Title Examples
- ❌ `Update`
- ❌ `Fix bug`
- ❌ `Changes`

### PR Description Should Include
- **What**: What changes did you make?
- **Why**: Why are these changes needed?
- **Testing**: How did you test the changes?

### Example PR Description
```markdown
## What
Added support for 10 new companies in the Cambridge area.

## Why
These companies actively hire interns and were missing from our list.

## Testing
- Ran `./run_all.sh` successfully
- Verified all company slugs are valid
- Checked that jobs appear in README without duplicates
```

## Common Issues & Solutions

### Issue: Company slug returns 404
**Solution**: The company might have changed their slug or doesn't use that job board. Try:
1. Search for the company's careers page
2. Check if they use a different job board
3. Verify the slug by visiting the URL directly

### Issue: Too many non-intern jobs appearing
**Solution**: Add exclude keywords to that company in `companies.yml`:
```yaml
exclude_keywords: ["senior", "staff", "principal", "lead"]
```

### Issue: Jobs not appearing in README
**Solution**: Check if:
1. Jobs match location filters (Boston area or Remote)
2. Jobs contain "intern" or "internship" keywords
3. Jobs aren't already in the README (duplicate detection)

## Feature Requests

Have an idea? Open an issue with:
- **Clear title**: "Feature Request: Add Slack notifications"
- **Description**: What feature you'd like and why
- **Use case**: How it would help you or others

## Questions?

Feel free to:
- Open an issue for questions
- Check existing issues for answers
- Review the code - it's well-commented!

## Code of Conduct

- Be respectful and constructive
- Help others learn
- Give credit where it's due
- Focus on making the tool better for everyone

---

**Thank you for contributing!** Every addition helps students find opportunities. 🎉
