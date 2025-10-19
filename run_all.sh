# Run all job search reports
set -e

cd ~/tech-internships-boston-area

# Load environment variables from .env if it exists
if [[ -f .env ]]; then
    source .env
fi

echo "=== Running Greenhouse/Lever Report ==="
python3 scripts/job_report.py --include-remote --config config/companies.yml

# Only run Adzuna if credentials are set
if [[ -n "$ADZUNA_APP_ID" && -n "$ADZUNA_APP_KEY" ]]; then
    echo ""
    echo "=== Running Adzuna Report ==="
    python3 scripts/adzuna_report.py \
        --what 'intern systems OR infrastructure OR backend OR reliability OR compiler OR quant OR simulation OR modeling OR "data infrastructure" OR "ml systems"' \
        --location "Boston, MA"
else
    echo ""
    echo "ℹ️  Skipping Adzuna (set ADZUNA_APP_ID and ADZUNA_APP_KEY to enable)"
fi

if [[ -n "$SERPAPI_KEY" ]]; then
    echo ""
    echo "=== Discovering New Company Slugs ==="
    python3 scripts/discover_slugs.py --max 50 --config config/companies.yml
else
    echo ""
    echo "ℹ️  Skipping slug discovery (set SERPAPI_KEY to enable)"
fi

echo ""
echo "=== Scraping SimplifyJobs Summer2026-Internships ==="
python3 scripts/simplify_scraper.py

echo ""
echo "=== Sorting README by date (newest first) ==="
python3 scripts/sort_readme.py

echo ""
echo "✅ Done! Check README.md for all job listings."
