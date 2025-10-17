#!/usr/bin/env bash
# Run all job search reports
set -e

cd ~/jobSearcher

# Load environment variables from .env if it exists
if [[ -f .env ]]; then
    source .env
fi

echo "=== Running Greenhouse/Lever Report ==="
python3 job_report.py --include-remote

# Only run Adzuna if credentials are set
if [[ -n "$ADZUNA_APP_ID" && -n "$ADZUNA_APP_KEY" ]]; then
    echo ""
    echo "=== Running Adzuna Report ==="
    python3 adzuna_report.py \
        --what "intern systems OR infrastructure OR backend OR reliability OR compiler OR quant OR simulation OR modeling OR 'data infrastructure' OR 'ml systems'" \
        --location "Boston, MA" \
        --remote
else
    echo ""
    echo "ℹ️  Skipping Adzuna (set ADZUNA_APP_ID and ADZUNA_APP_KEY to enable)"
fi

if [[ -n "$SERPAPI_KEY" ]]; then
    echo ""
    echo "=== Discovering New Company Slugs ==="
    python3 discover_slugs.py --max 50
else
    echo ""
    echo "ℹ️  Skipping slug discovery (set SERPAPI_KEY to enable)"
fi

echo ""
echo "✅ Done! Check ./reports/ for output"
