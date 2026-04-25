import schedule
import time
from datetime import datetime
from nav_scraper import get_nav, bondextra_url, growth_url
from nav_saved import log_navs, get_yesterday_nav
from nav_utils import breakeven_nav, compare_nav
from nav_email import send_email

def log_error(message, filename="error_log.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {message}\n")

def format_pl(value):
    """Format profit/loss with + sign for positives."""
    if value > 0:
        return f"+{value:,.2f}"
    else:
        return f"{value:,.2f}"

def format_pct(value):
    """Format percentage with + sign for positives."""
    if value > 0:
        return f"+{value:.2f}"
    else:
        return f"{value:.2f}"

def job(test_mode=False):
    try:
        # Scrape NAVs
        bond_nav = get_nav(bondextra_url)
        growth_nav = get_nav(growth_url)

        # Yesterday NAVs
        y_bond, y_growth = get_yesterday_nav()

        # Breakeven NAVs (EPF basis)
        bond_breakeven = breakeven_nav(16796.00, 26753.64)
        growth_breakeven = breakeven_nav(17000.00, 10321.88)

        # Compare NAVs
        bond_text = compare_nav(bond_nav, y_bond, bond_breakeven)
        growth_text = compare_nav(growth_nav, y_growth, growth_breakeven)

        # Log NAVs
        log_navs(bond_nav, growth_nav)

        # Convert NAVs to floats
        bond_val = float(bond_nav.replace("MYR","").strip())
        growth_val = float(growth_nav.replace("MYR","").strip())

        # Units held
        bond_units = 26753.64
        growth_units = 10321.88

        # EPF capitals (include service charge)
        bond_epf_capital = 16796.00
        growth_epf_capital = 17000.00

        # Kenanga capitals (exclude service charge)
        bond_kenanga_capital = 16268.89  
        growth_kenanga_capital = 16466.49 

        # Market values
        bond_market = round(bond_val * bond_units, 2)
        growth_market = round(growth_val * growth_units, 2)

        # EPF P/L
        bond_pl = round(bond_market - bond_epf_capital, 2)
        growth_pl = round(growth_market - growth_epf_capital, 2)

        bond_pct = round((bond_pl / bond_epf_capital) * 100, 2)
        growth_pct = round((growth_pl / growth_epf_capital) * 100, 2)

        # Kenanga P/L
        bond_kenanga_pl = round(bond_market - bond_kenanga_capital, 2)
        growth_kenanga_pl = round(growth_market - growth_kenanga_capital, 2)

        bond_kenanga_pct = round((bond_kenanga_pl / bond_kenanga_capital) * 100, 2)
        growth_kenanga_pct = round((growth_kenanga_pl / growth_kenanga_capital) * 100, 2)

        # Totals (EPF)
        total_capital = bond_epf_capital + growth_epf_capital
        total_market = bond_market + growth_market
        total_pl = bond_pl + growth_pl
        total_pct = round((total_pl / total_capital) * 100, 2)

        # Totals (Kenanga)
        total_kenanga_capital = bond_kenanga_capital + growth_kenanga_capital
        total_kenanga_market = bond_market + growth_market  # same NAV × units
        total_kenanga_pl = bond_kenanga_pl + growth_kenanga_pl
        total_kenanga_pct = round((total_kenanga_pl / total_kenanga_capital) * 100, 2)

        # Format numbers with +/– signs
        bond_units_fmt = "{:,.2f}".format(bond_units)
        bond_market_fmt = "{:,.2f}".format(bond_market)
        bond_pl_fmt = format_pl(bond_pl)
        bond_kenanga_pl_fmt = format_pl(bond_kenanga_pl)

        growth_units_fmt = "{:,.2f}".format(growth_units)
        growth_market_fmt = "{:,.2f}".format(growth_market)
        growth_pl_fmt = format_pl(growth_pl)
        growth_kenanga_pl_fmt = format_pl(growth_kenanga_pl)

        total_capital_fmt = "{:,.2f}".format(total_capital)
        total_market_fmt = "{:,.2f}".format(total_market)
        total_pl_fmt = format_pl(total_pl)
        total_kenanga_capital_fmt = "{:,.2f}".format(total_kenanga_capital)
        total_kenanga_market_fmt = "{:,.2f}".format(total_kenanga_market)
        total_kenanga_pl_fmt = format_pl(total_kenanga_pl)

        # Format percentages with +/– signs
        bond_pct = format_pct(bond_pct)
        growth_pct = format_pct(growth_pct)
        bond_kenanga_pct = format_pct(bond_kenanga_pct)
        growth_kenanga_pct = format_pct(growth_kenanga_pct)
        total_pct = format_pct(total_pct)
        total_kenanga_pct = format_pct(total_kenanga_pct)

        if test_mode:
            # Print values instead of sending email
            print("BondEXTRA:", bond_text)
            print("Growth Fund:", growth_text)
            print("Bond EPF P/L:", bond_pl_fmt, bond_pct)
            print("Bond Kenanga P/L:", bond_kenanga_pl_fmt, bond_kenanga_pct)
            print("Growth EPF P/L:", growth_pl_fmt, growth_pct)
            print("Growth Kenanga P/L:", growth_kenanga_pl_fmt, growth_kenanga_pct)
            print("Total EPF P/L:", total_pl_fmt, total_pct)
            print("Total Kenanga P/L:", total_kenanga_pl_fmt, total_kenanga_pct)
        else:
            # Send email
            send_email(
                bond_text, growth_text,
                bond_units_fmt, bond_market_fmt, bond_pl_fmt, bond_pct,
                bond_kenanga_pl_fmt, bond_kenanga_pct,
                growth_units_fmt, growth_market_fmt, growth_pl_fmt, growth_pct,
                growth_kenanga_pl_fmt, growth_kenanga_pct,
                total_capital_fmt, total_market_fmt, total_pl_fmt, total_pct,
                total_kenanga_capital_fmt, total_kenanga_market_fmt, total_kenanga_pl_fmt, total_kenanga_pct
            )

    except Exception as e:
        log_error(str(e))

if __name__ == "__main__":
    job(test_mode=False)  # flip to True for debugging
