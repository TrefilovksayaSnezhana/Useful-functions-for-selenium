import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

browser = webdriver.Firefox()
browser.get("http://suninjuly.github.io/find_xpath_form")
input1 = browser.find_element(By.TAG_NAME, 'input')
input1.send_keys("Снежка")
input2 = browser.find_element(By.NAME, 'last_name')
input2.send_keys("Какешка")
input3 = browser.find_element(By.CLASS_NAME,"city")
input3.send_keys("Минск")
input4 = browser.find_element(By.ID, "country")
input4.send_keys('Беларусь')

browser.find_element(By.XPATH, "//div/*[text()='Submit']").click()
time.sleep(10)
browser.quit()
