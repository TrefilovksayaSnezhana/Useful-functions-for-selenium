import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

browser = webdriver.Firefox()
link = "http://suninjuly.github.io/alert_accept.html"
#
browser.get(link)
browser.find_element(By.CSS_SELECTOR, "button.btn").click()
browser.switch_to.alert.accept()

time.sleep(10)
browser.quit()
