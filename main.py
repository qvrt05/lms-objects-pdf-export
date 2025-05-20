from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def export_as_pdf(record_id):
    url = f"https://sbdicerna-vault-training.veevavault.com/ui/#t/0TB000000000C01/V0C/{record_id}"
    print(f"Opening: {url}")
    driver.get(url)

    try:
        wait = WebDriverWait(driver, 10)

        # Step 1: Wait for the Actions menu button to appear and click it
        print("Waiting for actions button...")
        actions_button = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'button[aria-label="All Actions"]')
        ))
        print("Actions button found!")
        actions_button.click()

        print("Waiting for PDF button...")
        pdf_button = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'li.vv-action-bar-menu-item[data-value="exportToPdf"]')
        ))
        print("PDF button found!")
        pdf_button.click()
        time.sleep(5)  # Let download start if applicable

    except Exception as e:
        print(f"❌ Failed to export record {record_id}: {e}")

# Test with one record ID
record_ids = ['V0C000000001001']  # replace with your actual object IDs
for rid in record_ids:
    export_as_pdf(rid)

driver.quit()
