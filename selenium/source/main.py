# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from actions import click_element, input_text, get_input_value
# from utils import check_element_displayed, check_text_in_page
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager

# def setup_driver():
# 	service = Service(GeckoDriverManager().install())
# 	driver = webdriver.Firefox(service=service) 
# 	return driver

# def main():
#     # Setup the WebDriver
#     driver = setup_driver()
    
#     # Visit the DemoQA website
#     driver.get("https://demoqa.com/")

#     # Example: Click a button (e.g., 'Elements' tab)
#     click_element(driver, "//div[@class='card-body'][contains(text(),'Elements')]")
    
#     # Navigate to Text Box page
#     driver.get("https://demoqa.com/text-box")

#     # Example: Input text into the Name field
#     input_text(driver, "//input[@id='userName']", "John Doe")
    
#     # Example: Input email into the Email field
#     input_text(driver, "//input[@id='userEmail']", "johndoe@example.com")

#     # Example: Get value from the Name field
#     input_value = get_input_value(driver, "//input[@id='userName']")
#     print(f"Input field value for Name: {input_value}")

#     # Example: Check if an element is displayed (Check Submit button visibility)
#     if check_element_displayed(driver, "//button[@id='submit']"):
#         print("Submit button is displayed on the page")

#     # Example: Check if text is present in the page source
#     if check_text_in_page(driver, "John Doe"):
#         print("Text 'John Doe' is found in the page source")

#     # Quit the driver
#     driver.quit()

# if __name__ == "__main__":
#     main()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time

# Setup Firefox options (run headless if necessary)
options = Options()
# options.add_argument("--headless")  # Uncomment this for headless mode

# Set up the driver with WebDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

# Step 1: Open Wikipedia
driver.get("https://www.wikipedia.org/")
print("Page Title:", driver.title)

# Step 2: Click on the English Wikipedia link (the first language link)
english_link = driver.find_element(By.XPATH, "//strong[text()='English']")
english_link.click()
time.sleep(2)  # Wait for the page to load

# Step 3: Verify that the field contains data (we'll check the search bar here)
search_input = driver.find_element(By.NAME, "search")
search_input.send_keys("Python programming language")
search_input.send_keys(Keys.RETURN)  # Hit Enter to search

# Step 4: Verify that the search results page contains the expected content
time.sleep(2)  # Allow time for results to load
assert "Python (programming language)" in driver.title
print(f"Title after search: {driver.title}")

# Step 5: Use XPath with a function to find a non-direct element (e.g., the "History" link)
history_link = driver.find_element(By.XPATH, "//span[contains(text(), 'History')]")
print(f"Found 'History' link: {history_link.text}")

# Step 6: Check a specific condition (let's check if the page has the correct title)
assert "Python (programming language)" in driver.title
print("Page contains expected title.")

# Step 7: Clean up (close the browser)
driver.quit()

