from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from actions import click_element, input_text, get_input_value
from utils import check_element_displayed, check_text_in_page
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def setup_driver():
	service = Service(GeckoDriverManager().install())
	driver = webdriver.Firefox(service=service) 
	return driver

def main():
    # Setup the WebDriver
    driver = setup_driver()
    
    # Visit the DemoQA website
    driver.get("https://demoqa.com/")

    # Example: Click a button (e.g., 'Elements' tab)
    click_element(driver, "//div[@class='card-body'][contains(text(),'Elements')]")
    
    # Navigate to Text Box page
    driver.get("https://demoqa.com/text-box")

    # Example: Input text into the Name field
    input_text(driver, "//input[@id='userName']", "John Doe")
    
    # Example: Input email into the Email field
    input_text(driver, "//input[@id='userEmail']", "johndoe@example.com")

    # Example: Get value from the Name field
    input_value = get_input_value(driver, "//input[@id='userName']")
    print(f"Input field value for Name: {input_value}")

    # Example: Check if an element is displayed (Check Submit button visibility)
    if check_element_displayed(driver, "//button[@id='submit']"):
        print("Submit button is displayed on the page")

    # Example: Check if text is present in the page source
    if check_text_in_page(driver, "John Doe"):
        print("Text 'John Doe' is found in the page source")

    # Quit the driver
    driver.quit()

if __name__ == "__main__":
    main()

