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
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    try:
        nav_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='daily-nav']/h4"))
        )
        nav_value = nav_element.text.strip()
    except Exception as e:
        nav_value = f"NAV not found ({e})"
    finally:
        driver.quit()
    return nav_value

bondextra_url = "https://www.kenangainvestors.com.my/kenanga-bondextra-fund"
growth_url = "https://www.kenangainvestors.com.my/kenanga-growth-fund"

print("BondEXTRA NAV:", get_nav(bondextra_url))
print("Growth Fund NAV:", get_nav(growth_url))