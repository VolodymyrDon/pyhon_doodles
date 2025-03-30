from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from actions import click_element, input_text, get_input_value
from utils import check_element_displayed, check_text_in_page

def setup_driver():
    """Sets up the WebDriver with headless option"""
    options = Options()
    options.add_argument("--headless")  # Run without GUI
    driver = webdriver.Firefox(options=options)
    return driver

def main():
    # Setup the WebDriver
    driver = setup_driver()
    driver.get("https://example.com")

    # Example: Click a button
    click_element(driver, "//button[@id='exampleButton']")

    # Example: Input text into a field
    input_text(driver, "//input[@id='inputField']", "Test data")

    # Example: Get value from the input field
    input_value = get_input_value(driver, "//input[@id='inputField']")
    print(f"Input field value: {input_value}")

    # Example: Check if an element is displayed
    if check_element_displayed(driver, "//h1[text()='Welcome']"):
        print("Element is displayed on the page")

    # Example: Check if text is present in the page source
    if check_text_in_page(driver, "Welcome"):
        print("Text is found in the page source")

    # Quit the driver
    driver.quit()

if __name__ == "__main__":
    main()

