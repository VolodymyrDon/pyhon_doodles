from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Set Firefox options (headless mode for Termux)
options = Options()
options.add_argument("--headless")  

# Specify the Geckodriver path explicitly
geckodriver_path = "/data/data/com.termux/files/usr/bin/geckodriver"
service = Service(geckodriver_path)

# Initialize WebDriver with the specified service
driver = webdriver.Firefox(service=service, options=options)

# Open a webpage to test
driver.get("https://www.google.com")
print(driver.title)

# Close the browser
driver.quit()



