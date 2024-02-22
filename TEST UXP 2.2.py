import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

browser = webdriver.Firefox()
browser.get("http://172.18.2.2:9089/Browser/Login")
input1 = browser.find_element(By.ID, "userId")
input1.send_keys("SNEZHAANA2")
input2 = browser.find_element(By.ID, "password")
input2.send_keys("Trefsnezh1")
browser.find_element(By.NAME,"commit").click()
time.sleep(5)
input3 = browser.find_element(By.NAME, "WORKINGELEMENTS[1].NAVIGATION[1].COMMANDLINE")
input3.send_keys("FT,")
button = browser.find_element(By.ID, "BUT_3B224FD68CBCFA9126188")
button.click()
time.sleep(7)
button2 = browser.find_element(By.ID, "C1__BUT_59666E37CA98156F22153")
button2.click()
time.sleep(20)
input4 = browser.find_element(By.NAME, "C1__C2__C1__C1__C1__VERFUNDSTRANSFER[1].TRANSACTIONTYPE")
input4.send_keys("AC")
button3 = browser.find_element(By.ID, "C1__commit_version_button")
button3.click()
time.sleep(20)
browser.quit()