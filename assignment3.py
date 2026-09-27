from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


driver.get("https://testautomationpractice.blogspot.com/")


driver.maximize_window()


time.sleep(2)




name = driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder^='Enter N']"
)

name.send_keys("Srijon")

print("1. ^= Starts With selector - Name entered successfully")



email = driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder$='EMail']"
)

email.send_keys("srijon@gmail.com")

print("2. $= Ends With selector - Email entered successfully")


phone = driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder*='Phone']"
)

phone.send_keys("9876543210")

print("3. *= Contains selector - Phone entered successfully")



time.sleep(5)


driver.quit()