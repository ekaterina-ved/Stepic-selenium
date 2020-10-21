from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    buttom1 = browser.find_element_by_css_selector('[type="submit"]').click()
    # alert = browser.switch_to.alert
    # alert.accept()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    submit = browser.find_element_by_css_selector('[type = "submit"]').click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
finally:
    time.sleep(1)
    browser.quit()
