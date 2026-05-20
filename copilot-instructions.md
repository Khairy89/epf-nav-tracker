# EPF NAV Tracker Copilot Instructions

This repository is a Python project that scrapes EPF-related NAV values, computes breakeven and market values, and sends a daily email report.

## Key files
- `nav_scraper.py`: scrapes the latest NAV values
- `nav_saved.py`: stores and retrieves previous NAV history
- `nav_utils.py`: calculates breakeven, profit/loss, and formatting
- `nav_email.py`: formats and sends the daily email report
- `nav_scheduler.py`: orchestrates scraping, comparison, and email delivery

## Environment
- Python virtual environment: `venv/Scripts/python.exe`
- Dependencies: `requirements.txt`

## Recommended workflow
- Use Pylance analysis for Python diagnostics and completions
- Use Git access to inspect repo history, diffs, and status
- Use the integrated terminal to run tasks and commands

## Useful commands
- `venv\Scripts\activate`
- `python -m pip install -r requirements.txt`
- `python nav_scheduler.py`
- `python nav_scraper.py`

## Git context
- This repo is version controlled with Git
- Use `git status`, `git diff`, `git log`, and `git show` for change inspection

## Terminal context
- The workspace supports PowerShell as the default integrated terminal
- Tasks are available for dependency install and running the scheduler

## Pylance context
- Provide diagnostics and type hints across all Python files in the workspace
- Use the current repo structure and imports for accurate symbol resolution
