from selenium import webdriver
import unittest
import time


class test_find_element_true(unittest.TestCase):
    def test_true(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        input3.send_keys("1@2.ru")
        input4 = browser.find_element_by_css_selector('[placeholder="Input your phone:"]')
        input4.send_keys("123456789")
        input5 = browser.find_element_by_css_selector('[placeholder="Input your address:"]')
        input5.send_keys("1 st, 1-2")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
    def test_false(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        input3.send_keys("1@2.ru")
        input4 = browser.find_element_by_css_selector('[placeholder="Input your phone:"]')
        input4.send_keys("123456789")
        input5 = browser.find_element_by_css_selector('[placeholder="Input your address:"]')
        input5.send_keys("1 st, 1-2")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()
