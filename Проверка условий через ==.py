import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

browser = webdriver.Firefox()
browser.get('http://suninjuly.github.io/registration1.html')
#заполнение формы регистрации
input1 = browser.find_element(By.CLASS_NAME,"first")
input1.send_keys("Снежинка")
input2 = browser.find_element(By.CLASS_NAME,"second")
input2.send_keys("Трюфель")
input3 = browser.find_element(By.CLASS_NAME,"third")
input3.send_keys("огого@mail.ru")
#поиск кнопки и отправление формы регистрации
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
#проверка текста
welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
welcome_text: str = welcome_text_elt.text
assert "Congratulations! You have successfully registered!" == welcome_text

time.sleep(5)
browser.quit()
