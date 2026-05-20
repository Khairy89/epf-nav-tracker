# EPF NAV Tracker

A Python project that automatically scrapes daily Net Asset Values (NAV) for EPF unit trust funds, compares them with yesterday’s values, calculates breakeven NAV, market value, and unrealised profit/loss, then emails a formatted daily report.

---

## 🚀 Features
- Scrapes NAVs for Kenanga Shariah Growth Opportunities Fund and Growth Fund.
- Compares today’s NAV vs yesterday’s NAV with arrows (↑ ↓ →).
- Calculates breakeven NAV (capital ÷ units).
- Shows current market value and unrealised profit/loss (MYR + %).
- Displays both EPF (with service charge) and Kenanga (without service charge) profit/loss.
- Summarises total portfolio performance.
- Sends a clean HTML email with bullet points, color styling, and +/– signs for clarity.

---

## 📂 Project Structure

```text
epf-nav-tracker/
├── nav_scraper.py     # Scrapes NAV values
├── nav_saved.py       # Logs NAVs, retrieves yesterday's NAV
├── nav_utils.py       # Breakeven, compare_nav, formatting helpers
├── nav_email.py       # Formats + sends email (no calculations)
├── nav_scheduler.py   # Job runner, prepares data, calls send_email
├── requirements.txt   # Dependencies
└── README.md          # Documentation
```

---

## ⚙️ Setup Instructions
1. Clone the repo:
   git clone https://github.com/Khairy89/epf-nav-tracker.git
   cd epf-nav-tracker

2. Create a virtual environment:
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows

3. Install dependencies:
   pip install -r requirements.txt

4. Configure Gmail:
   - Enable 2FA on your Gmail account.
   - Generate an App Password.
   - Replace "your_app_password" in nav_email.py with the generated password.

5. Run the scheduler:
   python nav_scheduler.py

---

## 🔄 Updating Portfolio Details

If your fund manager updates your portfolio or units, adjust these values in nav_scheduler.py:

# Kenanga Shariah Growth Opportunities Fund
shariah_breakeven = breakeven_nav(16303.67, 11010.04)   # capital, units

# Growth Fund
growth_breakeven = breakeven_nav(17000.00, 10321.88) # capital, units

- Capital → update if you top up or withdraw.
- Units Held → update if your fund manager confirms new unit allocation.

These values are used to calculate breakeven NAV, market value, and profit/loss.

---

## 📧 Example Email Output

Daily NAV Update - 2026-05-21

Kenanga Shariah Growth Opportunities Fund
- NAV: MYR 1.4694 ↑ (+0.8600) - Yesterday: MYR 0.6094 (Breakeven: 1.4808)
- Units Held: 11,010.04
- Current Market Value (EPF): MYR 16,178.15
- Unrealised Profit/Loss (EPF): -125.52 (-0.77%)
- Unrealised Profit/Loss (Kenanga): -125.52 (-0.77%)

Growth Fund
- NAV: MYR 1.6670 → (0.0000) - Yesterday: MYR 1.6670 (Breakeven: 1.6470)
- Units Held: 10,321.88
- Current Market Value (EPF): MYR 17,198.81
- Unrealised Profit/Loss (EPF): +206.57 (+1.22%)
- Unrealised Profit/Loss (Kenanga): +740.08 (+4.49%)

Total Portfolio
- Total Capital (EPF): MYR 33,303.67
- Total Market Value (EPF): MYR 33,376.96
- Total Unrealised Profit/Loss (EPF): +81.05 (+0.24%)
- Total Unrealised Profit/Loss (Kenanga): +614.56 (+1.84%)

---

-------------------------

## 🕒 Automating with Windows Task Scheduler

To run the NAV tracker automatically every morning:

1. Open Task Scheduler (`taskschd.msc`).
2. Create a new task named "EPF NAV Tracker".
3. Set it to run daily at your chosen time (e.g. 9:00 AM).
4. Action: Start a program → `python nav_scheduler.py`.
5. Set "Start in" to your project folder path.
6. Enable "Run whether user is logged on or not" and "Wake the computer to run this task".
7. Save and test by right‑clicking → Run.

⚠️ If your Windows account has no password, background tasks may not run when logged out. Either set a password or keep the PC logged in.
