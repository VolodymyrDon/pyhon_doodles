from selenium.webdriver.common.by import By

def find_element_by_xpath(driver, xpath):
    """Function to find an element by its XPath"""
    return driver.find_element(By.XPATH, xpath)

def check_element_displayed(driver, xpath):
    """Check if an element is displayed on the page"""
    element = find_element_by_xpath(driver, xpath)
    return element.is_displayed()

def check_text_in_page(driver, text):
    """Check if the text is present on the page source"""
    return text in driver.page_source

