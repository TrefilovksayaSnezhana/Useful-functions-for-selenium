import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

browser: WebDriver = webdriver.Firefox()

try:
    browser.get("https://www.avito.ru/moskva/transport")
    time.sleep(2)

    items = browser.find_elements(By.XPATH,"//div[@data-marker='item-photo']")
    items[0].click()
    # print(driver.window_handles)
    time.sleep(5)

    browser.switch_to.window(browser.window_handles[1])
    time.sleep(5)
    print(f"Currently URL is: {browser.current_url}")

    username = browser.find_element(By.CLASS_NAME,"seller-info-name")
    print(f"User name is: {username.text}")
    print("#" * 20)
    time.sleep(5)

    browser.close()

    browser.switch_to.window(browser.window_handles[0])
    time.sleep(5)
    print(f"Currently URL is: {browser.current_url}")

    items[1].click()
    time.sleep(5)

    browser.switch_to.window(browser.window_handles[1])
    time.sleep(5)
    print(f"Currently URL is: {browser.current_url}")
    username = browser.find_element(By.XPATH,"//div[@data-marker='seller-info/name']")
    print(f"User name is: {username.text}")
    print("-" * 20)

    ad_date = driver.find_element(By.CLASS_NAME,"title-info-metadata-item-redesign")
    print(f"An ad date is: {ad_date.text}")
    print("-" * 20)

    joined_date = browser.find_elements(By.CLASS_NAME,"seller-info-value")[1]
    print(f"User since: {joined_date.text}")
    print("#" * 20)

    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()