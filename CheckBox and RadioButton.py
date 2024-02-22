import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

browser = webdriver.Firefox()
browser.get("https://suninjuly.github.io/math.html")
browser.find_element(By.CSS_SELECTOR, "[value='robots']").click()
browser.find_element(By.ID, 'robotCheckbox').click()
time.sleep(10)
browser.quit()
