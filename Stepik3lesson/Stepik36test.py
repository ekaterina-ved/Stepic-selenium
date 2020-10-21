import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestLessonText():
    @pytest.mark.parametrize('links_lesson', {"236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1",
                                              "236899/step/1", "236903/step/1", "236904/step/1", "236905/step/1"})
    def test_guest_should_see_login_link(self, browser, links_lesson):
        link = f"https://stepik.org/lesson/{links_lesson}"
        browser.get(link)
        browser.implicitly_wait(8)
        textArea: WebElement = browser.find_element_by_css_selector(".textarea")
        answer = math.log(int(time.time()))
        textArea.send_keys(str(answer))
        submit_button = browser.find_element_by_css_selector(".submit-submission")
        submit_button.click()
        info_message = browser.find_element_by_css_selector(".smart-hints__hint")
        assert info_message.text == "Correct!", info_message.text