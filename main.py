from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options to run headlessly
chrome_options = Options()
chrome_options.add_argument("--headless")  # Headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")  # Disable GPU (important for headless mode)
chrome_options.add_argument("--no-sandbox")  # Required for some environments

# Initialize the WebDriver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

# Function to export a record as PDF
def export_as_pdf(record_id):
    url = f"https://sbdicerna-vault-training.veevavault.com/api/v25.1/ui/#/lifesciences/person__v/{record_id}"
    
    # Navigate to the URL
    driver.get(url)
    time.sleep(3)  # Wait for the page to load (adjust time if necessary)

    # Locate the "Export as PDF" button (you might need to inspect and adjust this)
    try:
        # Assuming the button has a specific selector, adjust as necessary
        export_button = driver.find_element(By.CSS_SELECTOR, 'button.export-pdf')
        export_button.click()  # Click the button to trigger PDF export
        
        # Optionally, handle the print dialog if necessary
        # (this will depend on how the dialog is handled in your environment)

        time.sleep(5)  # Wait for the export to complete (adjust time if needed)
        print(f"Exported record {record_id} as PDF")

    except Exception as e:
        print(f"Failed to export record {record_id}: {e}")

# List of record IDs to loop through
record_ids = ['V16000000001001']  # Example IDs, replace with actual IDs

# Loop through record IDs and export them
for record_id in record_ids:
    export_as_pdf(record_id)

# Close the driver once done
driver.quit()
