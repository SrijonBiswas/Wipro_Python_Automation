from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create Chrome WebDriver
driver = webdriver.Chrome()

# Open Rahul Shetty Academy
driver.get("https://rahulshettyacademy.com")

# Maximize browser
driver.maximize_window()

# Wait for page to load
time.sleep(3)

# Locate child element using CSS Child Selector
element = driver.find_element(
    By.CSS_SELECTOR,
    "div > a"
)

# Display element information
print("Element located successfully!")
print("Tag Name:", element.tag_name)
print("Text:", element.text)
print("Link:", element.get_attribute("href"))

# Scroll the element into view
driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    element
)

time.sleep(1)

# Click the element using JavaScript
driver.execute_script(
    "arguments[0].click();",
    element
)

time.sleep(3)

# Close browser
driver.quit()