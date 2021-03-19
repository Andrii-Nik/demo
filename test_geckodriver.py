import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome("C:\\Users\\asdfg\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver\\chromedriver.exe")
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class TestLogin:
    def test_should_correct(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(5)
        answer = math.log(int(time.time()))
        input1 = browser.find_element_by_xpath("/html/body/div/div[1]/div[2]/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[2]/div/div/div/textarea")
        input1.send_keys(str(answer))
        button = browser.find_element_by_class_name('submit-submission').click()
        time.sleep(5)
        message = browser.find_element_by_class_name("smart-hints__hint")

        assert "Correct!" in message.text

