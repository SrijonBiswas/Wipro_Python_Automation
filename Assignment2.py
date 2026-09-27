from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def print_links_from_rahulshettyacademy() -> None:
    driver = webdriver.Edge()
    driver.get("https://rahulshettyacademy.com")
    driver.maximize_window()

    links = driver.find_elements(By.TAG_NAME, "a")

    for index, link in enumerate(links, start=1):
        text = link.text.strip()
        href = link.get_attribute("href")
        print(f"{index}. Text: '{text}' | URL: {href}")

    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    print_links_from_rahulshettyacademy()
