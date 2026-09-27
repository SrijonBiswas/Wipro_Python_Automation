from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

name = driver.find_element(By.ID, "name")
name.send_keys("John Doe")

email = driver.find_element(By.ID, "email")
email.send_keys("example@email.com")

phone = driver.find_element(By.ID, "phone")
phone.send_keys("123456")

address = driver.find_element(By.ID, "textarea")
address.send_keys("Kolkata, West Bengal")

time.sleep(10)




