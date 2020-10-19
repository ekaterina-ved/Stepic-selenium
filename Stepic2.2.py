from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1_element = browser.find_element_by_id("num1")
    num1 = num1_element.text
    num2_element = browser.find_element_by_id("num2")
    num2 = num2_element.text
    Summ = int(num1) + int(num2)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(Summ))
    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
