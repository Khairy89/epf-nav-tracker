# EPF NAV Tracker

A Python project that automatically scrapes daily Net Asset Values (NAV) for EPF unit trust funds, compares them with yesterday’s values, calculates breakeven NAV, market value, and unrealised profit/loss, then emails a formatted daily report.

---

## 🚀 Features
- Scrapes NAVs for BondEXTRA and Growth Fund.
- Compares today’s NAV vs yesterday’s NAV with arrows (↑ ↓ →).
- Calculates breakeven NAV (capital ÷ units).
- Shows current market value and unrealised profit/loss (MYR + %).
- Displays both EPF (with service charge) and Kenanga (without service charge) profit/loss.
- Summarises total portfolio performance.
- Sends a clean HTML email with bullet points, color styling, and +/– signs for clarity.

---

## 📂 Project Structure

epf-nav-tracker/
├── nav_scraper.py     # Scrapes NAV values
├── nav_saved.py       # Logs NAVs, retrieves yesterday's NAV
├── nav_utils.py       # Breakeven, compare_nav, formatting helpers
├── nav_email.py       # Formats + sends email (no calculations)
├── nav_scheduler.py   # Job runner, prepares data, calls send_email
├── requirements.txt   # Dependencies
└── README.md          # Documentation

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

# BondEXTRA Fund
bond_breakeven = breakeven_nav(16796.00, 26753.64)   # capital, units

# Growth Fund
growth_breakeven = breakeven_nav(17000.00, 10321.88) # capital, units

- Capital → update if you top up or withdraw.
- Units Held → update if your fund manager confirms new unit allocation.

These values are used to calculate breakeven NAV, market value, and profit/loss.

---

## 📧 Example Email Output

Daily NAV Update - 2026-04-25

BondEXTRA Fund
- NAV: MYR 0.6085 ↑ (+0.0001) - Yesterday: MYR 0.6084 (Breakeven: 0.6278)
- Units Held: 26,753.64
- Current Market Value (EPF): MYR 16,279.59
- Unrealised Profit/Loss (EPF): -516.41 (-3.07%)
- Unrealised Profit/Loss (Kenanga): +10.70 (+0.07%)

Growth Fund
- NAV: MYR 1.6347 ↑ (+0.0136) - Yesterday: MYR 1.6211 (Breakeven: 1.6470)
- Units Held: 10,321.88
- Current Market Value (EPF): MYR 16,873.18
- Unrealised Profit/Loss (EPF): -126.82 (-0.75%)
- Unrealised Profit/Loss (Kenanga): +406.69 (+2.47%)

Total Portfolio
- Total Capital (EPF): MYR 33,796.00
- Total Market Value (EPF): MYR 33,152.77
- Total Unrealised Profit/Loss (EPF): -643.23 (-1.90%)
- Total Unrealised Profit/Loss (Kenanga): +417.39 (+1.28%)
EOF

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
