from selenium import webdriver
import time
import math
import os
browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/execute_script.html"
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

# try:
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#     x_element = browser.find_element_by_id("input_value")
#     x = x_element.text
#     y = calc(x)
#     input1 = browser.find_element_by_id("answer")
#     input1.send_keys(y)
#     button = browser.find_element_by_tag_name("button")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     checkbox = browser.find_element_by_id("robotCheckbox")
#     checkbox.click()
#     radiobutton = browser.find_element_by_css_selector('[value="robots"]')
#     radiobutton.click()
# # button = browser.find_element_by_tag_name("button")
# # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# last exe download file
try:
    input_name = browser.find_element_by_name("firstname")
    input_name.send_keys("Ekaterina")
    input_last_name = browser.find_element_by_name("lastname")
    input_last_name.send_keys("Ved")
    input_email = browser.find_element_by_name("email")
    input_email.send_keys("444@ya.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'for 21.txt')           # добавляем к этому пути имя файла
    attach_file = browser.find_element_by_id("file")
    attach_file.send_keys(file_path)
    button = browser.find_element_by_css_selector('button[type="submit"]').click()
# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))
finally:
    time.sleep(10)
    browser.quit()