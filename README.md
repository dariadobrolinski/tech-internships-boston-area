# Boston Tech Internship Finder

An automated script to search and aggregate tech internship opportunities in the Boston area from multiple sources including Greenhouse, Lever, Adzuna, and Google Search (via SERP API).

I know this isn't perfect so if there are any issues feel free to contribute!

**[Setup Instructions](#setup-instructions)**

---

## Job Listings

| Company Name | Job Title | Location | Date Posted | APPLY |
|---|---|---|---|---|
| Formlabs | Hardware Test Engineering Intern (Winter/Spring 2026) | Somerville, MA | 10/16/2025 | [APPLY](https://careers.formlabs.com/job/7271951/apply/?gh_jid=7271951) |
| Formlabs | Program Management - Global Sourcing Intern (Winter/Spring 2026) | Boston, MA | 10/16/2025 | [APPLY](https://careers.formlabs.com/job/7190788/apply/?gh_jid=7190788) |
| Formlabs | Global Operations Sourcing Intern (Winter/Spring 2026) | Boston, MA | 10/16/2025 | [APPLY](https://careers.formlabs.com/job/7190913/apply/?gh_jid=7190913) |
| Formlabs | Hardware R&D Engineering Intern (Winter/Spring 2026) | Somerville, MA | 10/15/2025 | [APPLY](https://careers.formlabs.com/job/7233962/apply/?gh_jid=7233962) |
| CarGurus | Data Platform Engineer II | Boston, Massachusetts, United States | 10/15/2025 | [APPLY](https://careers.cargurus.com/us/en/job/7264613?gh_jid=7264613) |
| Cloudflare | Technical Support Engineer, Developer Platform | Distributed | 10/15/2025 | [APPLY](https://boards.greenhouse.io/cloudflare/jobs/7268796?gh_jid=7268796) |
| Formlabs | Manufacturing Engineering Intern (Spring/Summer 2026) | Somerville, MA | 10/14/2025 | [APPLY](https://careers.formlabs.com/job/7083351/apply/?gh_jid=7083351) |
| Formlabs | Manufacturing Test Software Intern (Winter/Spring 2026) | Somerville, MA | 10/14/2025 | [APPLY](https://careers.formlabs.com/job/7284267/apply/?gh_jid=7284267) |
| Formlabs | Industrial Design Intern (Winter/Spring 2026) | Somerville, MA | 10/14/2025 | [APPLY](https://careers.formlabs.com/job/7269786/apply/?gh_jid=7269786) |
| Formlabs | Electrical Engineering Intern (Winter/Spring 2026) | Somerville, MA | 10/10/2025 | [APPLY](https://careers.formlabs.com/job/7286400/apply/?gh_jid=7286400) |
| Formlabs | Build Team Intern (Winter/Spring 2026) | Somerville, MA | 10/08/2025 | [APPLY](https://careers.formlabs.com/job/7215024/apply/?gh_jid=7215024) |
| Formlabs | Mechanical Engineering Intern (Winter/Spring 2026) | Somerville, MA | 10/08/2025 | [APPLY](https://careers.formlabs.com/job/7095197/apply/?gh_jid=7095197) |
| Formlabs | People Analytics MBA Intern (Fall 2025 Part-Time) | Somerville, MA | 10/08/2025 | [APPLY](https://careers.formlabs.com/job/7263134/apply/?gh_jid=7263134) |
| Formlabs | Print Production Intern (Winter/Spring 2026) | Somerville, MA | 10/08/2025 | [APPLY](https://careers.formlabs.com/job/7217328/apply/?gh_jid=7217328) |
| Formlabs | Video Content Creator Intern (Winter/Spring 2026) | Somerville, MA | 10/08/2025 | [APPLY](https://careers.formlabs.com/job/7134956/apply/?gh_jid=7134956) |
| Datadog | Software Engineering Intern (Summer) | Boston, Massachusetts, USA; New York, New York, USA | 10/03/2025 | [APPLY](https://careers.datadoghq.com/detail/7158137/?gh_jid=7158137) |
| Datadog | Product Management Intern | New York, New York, USA | 10/03/2025 | [APPLY](https://careers.datadoghq.com/detail/7127832/?gh_jid=7127832) |
| Datadog | Cloud Researcher, Infrastructure Monitoring | New York, New York, USA | 10/01/2025 | [APPLY](https://careers.datadoghq.com/detail/7238269/?gh_jid=7238269) |

---

## Setup Instructions

### Prerequisites
- Python 3.7+
- pip (Python package manager)
- Git

### Clone the Repository
```bash
git clone https://github.com/dariadobrolinski/tech-internships-boston-area
cd tech-internships-boston-area
```

### Install Dependencies
```bash
pip install requests pyyaml
```

### Configure Environment Variables
Create a `.env` file in the root directory with your API keys:
```bash
# Optional: For Adzuna job search
ADZUNA_APP_ID=your_adzuna_app_id
ADZUNA_APP_KEY=your_adzuna_app_key

# Optional: For discovering new companies via Google Search
SERPAPI_KEY=your_serpapi_key
```

**Get API Keys:**
- **Adzuna**: Sign up at [adzuna.com/developers](https://developer.adzuna.com/)
- **SERP API**: Sign up at [serpapi.com](https://serpapi.com/)

> Note: The script will work with just Greenhouse/Lever searches even without API keys. The API keys are optional but enable additional job sources.

### Edit Configuration
Customize `companies.yml` to add/remove companies or adjust search keywords:
```yaml
companies:
  - name: YourCompany
    provider: greenhouse  # or "lever"
    slug: yourcompany-slug
    include_keywords: []
    exclude_keywords: []
```

### Run the Script
```bash
# Make the script executable
chmod +x run_all.sh

# Run all job searches
./run_all.sh
```

This will:
1. Search Greenhouse and Lever job boards for configured companies
2. (Optional) Search Adzuna for internships in the Boston area
3. (Optional) Discover new companies via Google Search
4. Append all results to `README.md`
5. Generate detailed reports in the `reports/` directory

### Customize Search Parameters
Edit `run_all.sh` to customize:
- **Keywords**: Change the search terms for Adzuna
- **Locations**: Modify Boston area cities
- **Remote jobs**: Add/remove `--include-remote` flag

### Automate with Cron (Optional)
Run daily at 9 AM:
```bash
crontab -e
# Add this line:
0 9 * * * cd ~/jobSearcher && ./run_all.sh >> ~/jobSearcher/cron.log 2>&1
```

---

**Happy job hunting! 🎉**
