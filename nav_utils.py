def breakeven_nav(investment_capital, units):
    """Calculate breakeven NAV (capital ÷ units)."""
    try:
        return round(float(investment_capital) / float(units), 4)
    except:
        return None

def compare_nav(today, yesterday, breakeven=None):
    """Compare today's NAV with yesterday's and format HTML string."""
    try:
        today_val = float(today.replace("MYR","").strip())
        if not yesterday:
            breakeven_text = f" (Breakeven: {breakeven})" if breakeven else ""
            return f"<span style='color:gray; font-weight:bold'>{today}</span> (no previous data){breakeven_text}"

        yesterday_val = float(yesterday.replace("MYR","").strip())
        diff = round(today_val - yesterday_val, 4)
        diff_str = f"+{diff}" if diff > 0 else str(diff)

        if today_val > yesterday_val:
            style, arrow = "color:green; font-weight:bold", "↑"
        elif today_val < yesterday_val:
            style, arrow = "color:red; font-weight:bold", "↓"
        else:
            style, arrow = "color:orange; font-weight:bold", "→"

        breakeven_text = f" (Breakeven: {breakeven})" if breakeven else ""
        return f"<span style='{style}'>{today} {arrow} ({diff_str})</span> - Yesterday: {yesterday}{breakeven_text}"
    except:
        return f"<span style='color:gray; font-weight:bold'>{today}</span> (comparison failed)"
