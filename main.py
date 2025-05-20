from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# === CONFIGURE CHROME OPTIONS ===
chrome_options = Options()
chrome_options.add_argument("--headless")             # Run in headless mode
chrome_options.add_argument("--disable-gpu")          # Recommended for headless
chrome_options.add_argument("--no-sandbox")           # Bypass OS security model
chrome_options.add_argument("--window-size=1920,1080")  # Ensure consistent viewport
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# === INIT WEBDRIVER ===
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# === PDF EXPORT FUNCTION ===
def export_as_pdf(record_id):
    # Vault UI URL
    url = f"https://sbdicerna-vault-training.veevavault.com/ui/#t/0TB000000000C01/V0C/{record_id}"
    print(f"Navigating to {url}")
    driver.get(url)
    
    # Wait for page to load
    time.sleep(5)

    try:
        # Locate the export PDF button using data-value attribute
        export_button = driver.find_element(
            By.CSS_SELECTOR,
            "li.vv-action-bar-menu-item[data-value='exportToPdf']"
        )
        
        export_button.click()
        print(f"Clicked 'Export as PDF' for record: {record_id}")
        
        # Allow some time for the export to be triggered
        time.sleep(5)

    except Exception as e:
        print(f"❌ Failed to export record {record_id}: {e}")

# === RECORDS TO EXPORT ===
record_ids = [
    "V0C000000001001",  # Add more record IDs as needed
]

# === LOOP THROUGH RECORDS ===
for record_id in record_ids:
    export_as_pdf(record_id)

# === CLEANUP ===
driver.quit()
print("✅ Done.")
