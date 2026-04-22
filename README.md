# EPF NAV Tracker

A Python project that automatically scrapes daily Net Asset Values (NAV) for EPF unit trust funds, compares them with yesterday’s values, calculates breakeven NAV, market value, and unrealised profit/loss, then emails a formatted daily report.

---

## 🚀 Features
- Scrapes NAVs for BondEXTRA and Growth Fund.
- Compares today’s NAV vs yesterday’s NAV with arrows (↑ ↓ →).
- Calculates breakeven NAV (capital ÷ units).
- Shows current market value and unrealised profit/loss (MYR + %).
- Summarises total portfolio performance.
- Sends a clean HTML email with bullet points and color styling.

---

## 📂 Project Structure

```
epf-nav-tracker/
├── nav_scraper.py     # Scrapes NAV values from fund URLs
├── nav_saved.py       # Logs NAVs and retrieves yesterday's NAV
├── nav_email.py       # Formats and sends email report
├── nav_scheduler.py   # Scheduler + job runner
├── requirements.txt   # Dependencies
└── README.md          # Documentation
```


---

## ⚙️ Setup Instructions
1. Clone the repo:
   ```bash
   git clone https://github.com/Khairy89/epf-nav-tracker.git
   cd epf-nav-tracker

2. Create a virtual environment:
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies: 
pip install -r requirements.txt

4. Configure Gmail:

Enable 2FA on your Gmail account.
Generate an App Password.
Replace "your_app_password" in nav_email.py with the generated password.

5. Run the scheduler


## Updating Portfolio Details

If your fund manager updates your portfolio or units, adjust these values in nav_scheduler.py:

# BondEXTRA Fund
bond_breakeven = breakeven_nav(16796.00, 26753.64)   # capital, units
send_email(..., 26753.64, 16796.00, ...)

# Growth Fund
growth_breakeven = breakeven_nav(17000.00, 10321.88) # capital, units
send_email(..., 10321.88, 17000.00, ...)

Capital → update if you top up or withdraw.

Units Held → update if your fund manager confirms new unit allocation.

These values are used to calculate breakeven NAV, market value, and profit/loss.

📧 Example Email Output

```
Daily NAV Update - 2026-04-22

BondEXTRA Fund
- NAV: MYR 0.6084 ↑ (+0.0001) - Yesterday: MYR 0.6083 (Breakeven: 0.6278)
- Units Held: 26,753.64
- Current Market Value: MYR 16,276.91
- Unrealised Profit/Loss: -519.09 (-3.09%)

Growth Fund
- NAV: MYR 1.6161 ↑ (+0.0006) - Yesterday: MYR 1.6155 (Breakeven: 1.6470)
- Units Held: 10,321.88
- Current Market Value: MYR 16,681.19
- Unrealised Profit/Loss: -318.81 (-1.88%)

Total Portfolio
- Total Capital: MYR 33,796.00
- Total Market Value: MYR 32,958.10
- Total Unrealised Profit/Loss: -837.90 (-2.48%)
```

---

👉 This README makes it clear where to change **capital** and **units** when your fund manager updates your portfolio. Do you want me to also add a **section on scheduling with Windows Task Scheduler** so the script runs automatically every morning without manual execution?