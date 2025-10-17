# API Keys Setup Guide

This guide will help you obtain and configure API keys for the job search script.

## Overview

The script works with three data sources:
1. **Greenhouse/Lever** - No API keys needed! ✅
2. **Adzuna** - Optional, for broader job search
3. **SERP API** - Optional, for discovering new companies

> **Note**: The script works great with just Greenhouse/Lever (no API keys needed). The other sources are optional enhancements.

---

## 🔑 Adzuna API Keys

### What is Adzuna?
Adzuna aggregates job listings from thousands of sources, giving you access to positions that might not be on Greenhouse or Lever.

### Why use it?
- Access to more job postings
- Broader coverage beyond tech-specific job boards
- Free tier is generous (generous rate limits)

### How to get keys

1. **Go to Adzuna Developer Portal**
   - Visit: https://developer.adzuna.com/

2. **Sign Up**
   - Click "Register" or "Sign Up"
   - Fill in your details (name, email, etc.)
   - Verify your email address

3. **Create an Application**
   - Once logged in, go to "My Applications"
   - Click "Create New Application"
   - Fill in the form:
     - **Application Name**: "Boston Internship Finder" (or your choice)
     - **Description**: "Personal project to aggregate tech internships"
     - **Usage**: Select "Personal/Academic"

4. **Get Your Keys**
   - After creating the application, you'll see:
     - **Application ID** (app_id)
     - **API Key** (app_key)
   - Copy both values

5. **Add to .env file**
   ```bash
   ADZUNA_APP_ID=your_app_id_here
   ADZUNA_APP_KEY=your_app_key_here
   ```

### Rate Limits
- **Free tier**: 250 calls per month
- Our script uses: ~1 call per run
- More than enough for daily or weekly searches!

---

## 🔍 SERP API Keys

### What is SERP API?
SERP API lets you programmatically search Google to discover new companies with job boards.

### Why use it?
- Automatically discover new companies hiring in Boston
- Finds companies you might not know about
- Keeps your company list fresh

### How to get keys

1. **Go to SERP API**
   - Visit: https://serpapi.com/

2. **Sign Up**
   - Click "Register" or "Sign Up"
   - You can sign up with:
     - Email
     - Google account
     - GitHub account

3. **Get Your API Key**
   - After signing up, go to your dashboard
   - You'll see your **API Key** immediately
   - Click "Copy" to copy it

4. **Add to .env file**
   ```bash
   SERPAPI_KEY=your_serp_api_key_here
   ```

### Rate Limits
- **Free tier**: 100 searches per month
- Our script uses: ~10-50 searches per run (configurable with `--max` flag)
- Perfect for occasional company discovery!

### Tips
- Start with `--max 20` to use fewer searches
- Run company discovery weekly, not daily
- The free tier is plenty for personal use

---

## 📝 Setting Up Your .env File

1. **Create .env file** in the project root:
   ```bash
   touch .env
   ```

2. **Add your keys** (use nano, vim, or any text editor):
   ```bash
   # Adzuna (optional)
   ADZUNA_APP_ID=your_adzuna_app_id
   ADZUNA_APP_KEY=your_adzuna_app_key

   # SERP API (optional)
   SERPAPI_KEY=your_serpapi_key
   ```

3. **Save and close** the file

4. **Verify** it's in .gitignore:
   ```bash
   cat .gitignore | grep .env
   ```
   Should show `.env` (so you don't accidentally commit your keys!)

---

## 🧪 Testing Your API Keys

### Test Adzuna
```bash
python3 scripts/adzuna_report.py --location "Boston, MA"
```

If successful, you'll see:
```
Found X results from Adzuna.
README.md: Added Y new jobs, skipped Z duplicates.
```

### Test SERP API
```bash
python3 scripts/discover_slugs.py --max 10
```

If successful, you'll see:
```
Greenhouse slugs: [...]
Lever slugs: [...]
Updated config/companies.yml with X total companies.
```

---

## ❌ Troubleshooting

### "Set ADZUNA_APP_ID and ADZUNA_APP_KEY in your environment"
**Problem**: API keys not found

**Solutions**:
1. Check `.env` file exists in the project root
2. Check keys are spelled correctly (no spaces)
3. Try running with keys directly:
   ```bash
   ADZUNA_APP_ID=xxx ADZUNA_APP_KEY=yyy ./run_all.sh
   ```

### "401 Unauthorized" or "403 Forbidden"
**Problem**: Invalid API keys

**Solutions**:
1. Double-check you copied the full key (no truncation)
2. Regenerate keys on the provider's website
3. Check if you've exceeded rate limits

### "400 Bad Request" from Adzuna
**Problem**: Invalid search query

**Solutions**:
1. This is usually a query syntax issue
2. Try simplifying the search terms
3. Check that the script is using double quotes (`"`) not single quotes (`'`) in the query

### "Too Many Requests" (429 error)
**Problem**: Hit rate limit

**Solutions**:
1. Wait until next month (free tier resets)
2. Reduce search frequency
3. For SERP: Use `--max 10` instead of default 50
4. Consider upgrading to paid tier if needed

---

## 💡 Tips & Best Practices

### Security
- ✅ **Never** commit `.env` to GitHub
- ✅ Keep your keys private
- ✅ Regenerate keys if accidentally exposed
- ❌ Don't share keys in issues or PRs

### Cost Management
- Use the free tiers - they're sufficient for personal use
- Run Adzuna searches daily (only 30 calls/month)
- Run SERP discovery weekly (saves API calls)
- Monitor your usage on provider dashboards

### Optimization
- **Adzuna**: Adjust `--max-days-old` to filter recent postings only
- **SERP**: Use `--max 20` for fewer API calls
- Both can be disabled by not setting the keys

---

## 📊 Feature Comparison

| Feature | No API Keys | + Adzuna | + SERP API | All Keys |
|---------|-------------|----------|------------|----------|
| Greenhouse/Lever jobs | ✅ | ✅ | ✅ | ✅ |
| Known companies only | ✅ | ✅ | ❌ | ❌ |
| Broader job search | ❌ | ✅ | ❌ | ✅ |
| Auto-discover companies | ❌ | ❌ | ✅ | ✅ |
| **Best for** | Starting out | More jobs | Growing list | Maximum coverage |

---

## 🆘 Need Help?

- **Check the main README**: Setup instructions
- **Review CONTRIBUTING.md**: Guidelines for issues
- **Open an issue**: Describe your problem with:
  - What you tried
  - Error messages
  - Your setup (OS, Python version)

---

**Happy job hunting!** 🎉
