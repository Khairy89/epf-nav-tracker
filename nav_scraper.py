import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_nav(url):
    chromedriver_autoinstaller.install()
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    try:
        nav_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'daily-nav')]//h4"))
        )
        nav_value = nav_element.text.strip()
        if not nav_value.startswith("MYR "):
            nav_value = f"MYR {nav_value}"
    except Exception as e:
        nav_value = f"NAV not found ({e})"
    finally:
        driver.quit()
    return nav_value

shariah_growth_url = "https://www.kenangainvestors.com.my/kenanga-shariah-growth-opportunity-fund"
growth_url = "https://www.kenangainvestors.com.my/kenanga-growth-fund"

# print("Shariah NAV:", get_nav(shariah_growth_url))
# print("Growth Fund NAV:", get_nav(growth_url))