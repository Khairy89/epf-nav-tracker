from datetime import datetime
import smtplib
from email.mime.text import MIMEText

def send_email(shariah_text, growth_text,
               shariah_units_fmt, shariah_market_fmt, shariah_pl_fmt, shariah_pct,
               shariah_kenanga_pl_fmt, shariah_kenanga_pct,
               growth_units_fmt, growth_market_fmt, growth_pl_fmt, growth_pct,
               growth_kenanga_pl_fmt, growth_kenanga_pct,
               total_capital_fmt, total_market_fmt, total_pl_fmt, total_pct,
               total_kenanga_capital_fmt, total_kenanga_market_fmt, total_kenanga_pl_fmt, total_kenanga_pct,
               shariah_daily_change_fmt, growth_daily_change_fmt):
    """Format and send the daily NAV email."""
    today = datetime.now().strftime("%Y-%m-%d")

    body = f"""<html>
    <body style="font-family:Arial, sans-serif; font-size:14px;">
        <h3>Daily NAV Update - {today}</h3>

        <h4><u>Kenanga Shariah Growth Opportunities Fund</u></h4>
        <ul>
            <li><b>NAV:</b> {shariah_text}</li>
            <li><b>Daily Change (MYR):</b>
                <span style="color:{'green' if float(shariah_daily_change_fmt.replace(',',''))>=0 else 'red'}; font-weight:bold">
                {shariah_daily_change_fmt}
                </span>
            </li>
            <li><b>Units Held:</b> {shariah_units_fmt}</li>
            <li><b>Current Market Value (EPF):</b> MYR {shariah_market_fmt}</li>
            <li><b>Unrealised Profit/Loss (EPF):</b>
                <span style="color:{'green' if float(shariah_pl_fmt.replace(',',''))>=0 else 'red'}; font-weight:bold">
                {shariah_pl_fmt} ({shariah_pct}%)
                </span>
            </li>
            <li><b>Unrealised Profit/Loss (Kenanga):</b>
                <span style="color:{'green' if float(shariah_kenanga_pl_fmt.replace(',',''))>=0 else 'red'}; font-weight:bold">
                {shariah_kenanga_pl_fmt} ({shariah_kenanga_pct}%)
                </span>
            </li>
        </ul>

        <h4><u>Growth Fund</u></h4>
        <ul>
            <li><b>NAV:</b> {growth_text}</li>
            <li><b>Daily Change (MYR):</b>
                <span style="color:{'green' if float(growth_daily_change_fmt.replace(',',''))>=0 else 'red'}; font-weight:bold">
                {growth_daily_change_fmt}
                </span>
            </li>
            <li><b>Units Held:</b> {growth_units_fmt}</li>
            <li><b>Current Market Value (EPF):</b> MYR {growth_market_fmt}</li>
            <li><b>Unrealised Profit/Loss (EPF):</b>
                <span style="color:{'green' if float(growth_pl_fmt.replace(',',''))>=0 else 'red'}; font-weight:bold">
                {growth_pl_fmt} ({growth_pct}%)
                </span>
            </li>
            <li><b>Unrealised Profit/Loss (Kenanga):</b>
                <span style="color:{'green' if float(growth_kenanga_pl_fmt.replace(',',''))>=0 else 'red'}; font-weight:bold">
                {growth_kenanga_pl_fmt} ({growth_kenanga_pct}%)
                </span>
            </li>
        </ul>

        <h4><u>Total Portfolio</u></h4>
        <ul>
            <li><b>Total Capital (EPF):</b> MYR {total_capital_fmt}</li>
            <li><b>Total Market Value (EPF):</b> MYR {total_market_fmt}</li>
            <li><b>Total Unrealised Profit/Loss (EPF):</b>
                <span style="color:{'green' if float(total_pl_fmt.replace(',',''))>=0 else 'red'}; font-weight:bold">
                {total_pl_fmt} ({total_pct}%)
                </span>
            </li>
            <li><b>Total Unrealised Profit/Loss (Kenanga):</b>
                <span style="color:{'green' if float(total_kenanga_pl_fmt.replace(',',''))>=0 else 'red'}; font-weight:bold">
                {total_kenanga_pl_fmt} ({total_kenanga_pct}%)
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
