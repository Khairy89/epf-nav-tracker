import csv
from datetime import datetime
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
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            rows = list(csv.reader(file))
            # rows[0] = header, rows[1:] = data
            if len(rows) > 2:  # header + at least 2 data rows
                return rows[-2][1], rows[-2][2]  # yesterday = second-last data row
            elif len(rows) == 2:  # header + only one data row
                return rows[-1][1], rows[-1][2]  # treat that single row as yesterday
    except FileNotFoundError:
        return None, None
    return None, None