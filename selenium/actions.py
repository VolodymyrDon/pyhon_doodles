from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def click_element(driver, xpath):
    """Function to click an element"""
    element = driver.find_element(By.XPATH, xpath)
    element.click()

def input_text(driver, xpath, text):
    """Function to input text into a field"""
    input_field = driver.find_element(By.XPATH, xpath)
    input_field.send_keys(text)

def get_input_value(driver, xpath):
    """Function to get the value from an input field"""
    input_field = driver.find_element(By.XPATH, xpath)
    return input_field.get_attribute("value")

