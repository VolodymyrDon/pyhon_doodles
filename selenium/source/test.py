from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Automatically downloads and manages GeckoDriver
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://www.google.com")
print("Page Title:", driver.title)

driver.quit()

