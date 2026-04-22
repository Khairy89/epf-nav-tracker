# EPF NAV Tracker Setup Guide

This document provides step-by-step instructions to set up your NAV scraping project in VS Code with GitHub.

---

## 1. Create GitHub Repository
1. Log in to [GitHub](https://github.com).
2. Click **New Repository**.
3. Name it `epf-nav-tracker`.
4. Initialize with a **README.md**.
5. Click **Create Repository**.

---

## 2. Clone Repo into VS Code
```bash
git clone https://github.com/yourname/epf-nav-tracker.git
cd epf-nav-tracker

# Ensure pip is installed globally
python -m ensurepip --upgrade
python -m pip install --upgrade pip setuptools wheel

# Delete old venv if it exists
rmdir venv /s /q

# Recreate venv
python -m venv venv

# Activate venv
venv\Scripts\activate

pip install requests beautifulsoup4 selenium schedule

import requests
from bs4 import BeautifulSoup

def get_nav(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    nav_element = soup.find("div", string=lambda t: t and "Latest NAV Price" in t)
    return nav_element.text if nav_element else "NAV not found"

bondextra_url = "https://www.fsmone.com.my/funds/tools/factsheet/kenanga-bondextra-fund?fund=MYKNGKBE"
growth_url = "https://www.fsmone.com.my/funds/tools/factsheet/kenanga-growth-fund?fund=MYKNGGF"

print("BondEXTRA NAV:", get_nav(bondextra_url))
print("Growth Fund NAV:", get_nav(growth_url))

import schedule, time

def job():
    print("Fetching NAVs...")
    # call get_nav() here

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)

git add .
git commit -m "Initial NAV scraper"
git push origin main
