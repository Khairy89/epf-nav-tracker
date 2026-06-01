import schedule
import time
from datetime import datetime
from nav_scraper import get_nav, shariah_growth_url, growth_url
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

def safe_print(*args, **kwargs):
    """Print with Windows console encoding safe."""
    safe_args = []
    for arg in args:
        if isinstance(arg, str):
            safe_args.append(arg.encode('ascii', 'backslashreplace').decode('ascii'))
        else:
            safe_args.append(arg)
    print(*safe_args, **kwargs)

def job(test_mode=False):
    try:
        # Scrape NAVs
        shariah_nav = get_nav(shariah_growth_url)
        growth_nav = get_nav(growth_url)

        # Yesterday NAVs
        y_shariah, y_growth = get_yesterday_nav()

        # Breakeven NAVs (EPF basis)
        shariah_breakeven = breakeven_nav(16303.67, 11010.04)
        growth_breakeven = breakeven_nav(17000.00, 10321.88)

        # Compare NAVs
        shariah_text = compare_nav(shariah_nav, y_shariah, shariah_breakeven)
        growth_text = compare_nav(growth_nav, y_growth, growth_breakeven)

        # Log NAVs
        log_navs(shariah_nav, growth_nav)

        # Convert NAVs to floats
        shariah_val = float(shariah_nav.replace("MYR"," ").strip())
        growth_val = float(growth_nav.replace("MYR"," ").strip())

        # Units held (updated for Kenanga Shariah Growth Opportunities Fund)
        shariah_units = 11010.04
        growth_dividend_units = 408.93  # Set to 0 if no dividends received yet
        growth_units = 10321.88 + growth_dividend_units  # Add dividend units to total growth units

        # EPF capitals (include service charge)
        shariah_epf_capital = 16303.67
        growth_epf_capital = 17000.00

        # Kenanga capitals (exclude service charge)
        # For the new Shariah position, use the current purchased capital here.
        # Update if you have a different service-charge-free amount.
        shariah_kenanga_capital = 16303.67
        growth_kenanga_capital = 16466.49

        # Market values
        shariah_market = round(shariah_val * shariah_units, 2)
        growth_market = round(growth_val * growth_units, 2)

        # EPF P/L
        shariah_pl = round(shariah_market - shariah_epf_capital, 2)
        growth_pl = round(growth_market - growth_epf_capital, 2)

        shariah_pct = round((shariah_pl / shariah_epf_capital) * 100, 2)
        growth_pct = round((growth_pl / growth_epf_capital) * 100, 2)

        # Kenanga P/L
        shariah_kenanga_pl = round(shariah_market - shariah_kenanga_capital, 2)
        growth_kenanga_pl = round(growth_market - growth_kenanga_capital, 2)

        shariah_kenanga_pct = round((shariah_kenanga_pl / shariah_kenanga_capital) * 100, 2)
        growth_kenanga_pct = round((growth_kenanga_pl / growth_kenanga_capital) * 100, 2)

        # Totals (EPF)
        total_capital = shariah_epf_capital + growth_epf_capital
        total_market = shariah_market + growth_market
        total_pl = shariah_pl + growth_pl
        total_pct = round((total_pl / total_capital) * 100, 2)

        # Totals (Kenanga)
        total_kenanga_capital = shariah_kenanga_capital + growth_kenanga_capital
        total_kenanga_market = shariah_market + growth_market
        total_kenanga_pl = shariah_kenanga_pl + growth_kenanga_pl
        total_kenanga_pct = round((total_kenanga_pl / total_kenanga_capital) * 100, 2)

        # Format numbers with +/– signs
        shariah_units_fmt = "{:,.2f}".format(shariah_units)
        shariah_market_fmt = "{:,.2f}".format(shariah_market)
        shariah_pl_fmt = format_pl(shariah_pl)
        shariah_kenanga_pl_fmt = format_pl(shariah_kenanga_pl)

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
        shariah_pct = format_pct(shariah_pct)
        growth_pct = format_pct(growth_pct)
        shariah_kenanga_pct = format_pct(shariah_kenanga_pct)
        growth_kenanga_pct = format_pct(growth_kenanga_pct)
        total_pct = format_pct(total_pct)
        total_kenanga_pct = format_pct(total_kenanga_pct)

        # Calculate daily NAV changes (today NAV - yesterday NAV) × units
        y_shariah_val = float(str(y_shariah).replace("MYR", " ").strip())
        y_growth_val = float(str(y_growth).replace("MYR", " ").strip())
        shariah_daily_change = round((shariah_val - y_shariah_val) * shariah_units, 2)
        growth_daily_change = round((growth_val - y_growth_val) * growth_units, 2)
        shariah_daily_change_fmt = format_pl(shariah_daily_change)
        growth_daily_change_fmt = format_pl(growth_daily_change)

        if test_mode:
            # Print values instead of sending email
            safe_print("Kenanga Shariah Growth:", shariah_text)
            safe_print("Growth Fund:", growth_text)
            safe_print("\n--- Daily MYR Changes ---")
            safe_print("Today Shariah Fund (MYR):", shariah_daily_change_fmt)
            safe_print("Today Growth Fund (MYR):", growth_daily_change_fmt)
            safe_print("\n--- EPF Profit/Loss ---")
            safe_print("Shariah EPF P/L:", shariah_pl_fmt, shariah_pct)
            safe_print("Growth EPF P/L:", growth_pl_fmt, growth_pct)
            safe_print("\n--- Kenanga Profit/Loss ---")
            safe_print("Shariah Kenanga P/L:", shariah_kenanga_pl_fmt, shariah_kenanga_pct)
            safe_print("Growth Kenanga P/L:", growth_kenanga_pl_fmt, growth_kenanga_pct)
            safe_print("\n--- Portfolio Totals ---")
            safe_print("Total EPF P/L:", total_pl_fmt, total_pct)
            safe_print("Total Kenanga P/L:", total_kenanga_pl_fmt, total_kenanga_pct)
        else:
            # Send email
            send_email(
                shariah_text, growth_text,
                shariah_units_fmt, shariah_market_fmt, shariah_pl_fmt, shariah_pct,
                shariah_kenanga_pl_fmt, shariah_kenanga_pct,
                growth_units_fmt, growth_market_fmt, growth_pl_fmt, growth_pct,
                growth_kenanga_pl_fmt, growth_kenanga_pct,
                total_capital_fmt, total_market_fmt, total_pl_fmt, total_pct,
                total_kenanga_capital_fmt, total_kenanga_market_fmt, total_kenanga_pl_fmt, total_kenanga_pct,
                shariah_daily_change_fmt, growth_daily_change_fmt
            )

    except Exception as e:
        log_error(str(e))

if __name__ == "__main__":
    job(test_mode=False)  # flip to True for debugging
