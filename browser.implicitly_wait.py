import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()

message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text
time.sleep(10)
browser.quit()