import csv
from datetime import datetime, timedelta
import os

def log_navs(bond_nav, growth_nav, filename="nav_log.csv"):
    today = datetime.now().strftime("%Y-%m-%d")
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "BondEXTRA NAV", "Growth Fund NAV"])
        writer.writerow([today, bond_nav, growth_nav])

def get_yesterday_nav(filename="nav_log.csv"):
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            rows = list(csv.DictReader(file))
            # Try exact yesterday first
            for row in rows:
                if row["Date"] == yesterday:
                    return row["BondEXTRA NAV"], row["Growth Fund NAV"]
            # Fallback: last available date before yesterday
            for row in reversed(rows):
                if row["Date"] < yesterday:
                    return row["BondEXTRA NAV"], row["Growth Fund NAV"]
    except FileNotFoundError:
        return None, None
    return None, None