import schedule
import time
from datetime import datetime
from nav_scraper import get_nav, bondextra_url, growth_url
from nav_saved import log_navs, get_yesterday_nav
from nav_email import compare_nav, send_email, breakeven_nav

def log_error(message, filename="error_log.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {message}\n")

def job():
    try:
        bond_nav = get_nav(bondextra_url)
        growth_nav = get_nav(growth_url)

        print("BondEXTRA NAV:", bond_nav)
        print("Growth Fund NAV:", growth_nav)

        # Get yesterday's NAV BEFORE logging today's
        y_bond, y_growth = get_yesterday_nav()
        print("Yesterday BondEXTRA NAV:", y_bond)
        print("Yesterday Growth Fund NAV:", y_growth)

        # Calculate breakeven NAVs (EPF capital ÷ units)
        bond_breakeven = breakeven_nav(16796.00, 26753.64)
        growth_breakeven = breakeven_nav(17000.00, 10321.88)

        print("Bond breakeven NAV:", bond_breakeven)
        print("Growth breakeven NAV:", growth_breakeven)

        # Compare with breakeven included
        bond_text = compare_nav(bond_nav, y_bond, bond_breakeven)
        growth_text = compare_nav(growth_nav, y_growth, growth_breakeven)

        # Log today's NAVs
        log_navs(bond_nav, growth_nav)

        # Send email
        send_email(
        bond_text, growth_text,
        26753.64, 16796.00,   # Bond units, EPF capital
        10321.88, 17000.00,   # Growth units, EPF capital    
        bond_nav, growth_nav  # raw NAV values    
        )

    except Exception as e:
        log_error(str(e))

if __name__ == "__main__":
    job()