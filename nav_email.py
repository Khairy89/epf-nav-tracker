from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# Breakeven NAV calculator
def breakeven_nav(investment_capital, units):
    try:
        return round(float(investment_capital) / float(units), 4)
    except:
        return None
    

def compare_nav(today, yesterday, breakeven=None):
    try:
        today_val = float(today.replace("MYR","").strip())
        if not yesterday:
            breakeven_text = f" (Breakeven: {breakeven})" if breakeven else ""
            return f"<span style='color:gray; font-weight:bold'>{today}</span> (no previous data){breakeven_text}"

        yesterday_val = float(yesterday.replace("MYR","").strip())
        diff = round(today_val - yesterday_val, 4)
        diff_str = f"+{diff}" if diff > 0 else str(diff)

        if today_val > yesterday_val:
            style = "color:green; font-weight:bold"
            arrow = "↑"
        elif today_val < yesterday_val:
            style = "color:red; font-weight:bold"
            arrow = "↓"
        else:
            style = "color:orange; font-weight:bold"
            arrow = "→"

        breakeven_text = f" (Breakeven: {breakeven})" if breakeven else ""
        return f"<span style='{style}'>{today} {arrow} ({diff_str})</span> - Yesterday: {yesterday}{breakeven_text}"
    except:
        return f"<span style='color:gray; font-weight:bold'>{today}</span> (comparison failed)"


def send_email(bond_text, growth_text,
               bond_units, bond_capital,
               growth_units, growth_capital,
               bond_nav, growth_nav):
    today = datetime.now().strftime("%Y-%m-%d")

    # Raw NAV values
    bond_val = float(bond_nav.replace("MYR","").strip())
    growth_val = float(growth_nav.replace("MYR","").strip())

    # Market values
    bond_market = round(bond_val * bond_units, 2)
    growth_market = round(growth_val * growth_units, 2)

    # P/L
    bond_pl = round(bond_market - bond_capital, 2)
    growth_pl = round(growth_market - growth_capital, 2)

    # Percentages
    bond_pct = round((bond_pl / bond_capital) * 100, 2)
    growth_pct = round((growth_pl / growth_capital) * 100, 2)

    # Totals
    total_capital = bond_capital + growth_capital
    total_market = bond_market + growth_market
    total_pl = round(bond_pl + growth_pl, 2)
    total_pct = round((total_pl / total_capital) * 100, 2)

    # Format numbers with commas and 2 decimals
    bond_units_fmt = "{:,.2f}".format(bond_units)
    bond_market_fmt = "{:,.2f}".format(bond_market)
    bond_pl_fmt = "{:,.2f}".format(bond_pl)

    growth_units_fmt = "{:,.2f}".format(growth_units)
    growth_market_fmt = "{:,.2f}".format(growth_market)
    growth_pl_fmt = "{:,.2f}".format(growth_pl)

    total_capital_fmt = "{:,.2f}".format(total_capital)
    total_market_fmt = "{:,.2f}".format(total_market)
    total_pl_fmt = "{:,.2f}".format(total_pl)

    body = f"""<html>
    <body>
        <h3>Daily NAV Update - {today}</h3>

        <h4><u>BondEXTRA Fund</u></h4>
        <ul>
            <li><b>NAV:</b> {bond_text}</li>
            <li><b>Units Held:</b> {bond_units_fmt}</li>
            <li><b>Current Market Value:</b> MYR {bond_market_fmt}</li>
            <li><b>Unrealised Profit/Loss:</b>
                <span style="color:{'green' if bond_pl>=0 else 'red'}; font-weight:bold">
                {bond_pl_fmt} ({bond_pct}%)
                </span>
            </li>
        </ul>

        <h4><u>Growth Fund</u></h4>
        <ul>
            <li><b>NAV:</b> {growth_text}</li>
            <li><b>Units Held:</b> {growth_units_fmt}</li>
            <li><b>Current Market Value:</b> MYR {growth_market_fmt}</li>
            <li><b>Unrealised Profit/Loss:</b>
                <span style="color:{'green' if growth_pl>=0 else 'red'}; font-weight:bold">
                {growth_pl_fmt} ({growth_pct}%)
                </span>
            </li>
        </ul>

        <h4><u>Total Portfolio</u></h4>
        <ul>
            <li><b>Total Capital:</b> MYR {total_capital_fmt}</li>
            <li><b>Total Market Value:</b> MYR {total_market_fmt}</li>
            <li><b>Total Unrealised Profit/Loss:</b>
                <span style="color:{'green' if total_pl>=0 else 'red'}; font-weight:bold">
                {total_pl_fmt} ({total_pct}%)
                </span>
            </li>
        </ul>
    </body>
</html>"""

    msg = MIMEText(body, "html")
    msg["Subject"] = f"Daily NAV Update - {today}"
    msg["From"] = "mk.developeer@gmail.com"
    msg["To"] = "khairy.fauzi@gmail.com"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("mk.developeer@gmail.com", "qngt maaq gkjz hqnn")
        server.send_message(msg)
        print("Email sent successfully")
