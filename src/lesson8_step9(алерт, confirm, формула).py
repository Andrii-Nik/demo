from selenium import webdriver
import time
import math
import os

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome("C:\\Users\\asdfg\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver\\chromedriver.exe")
    browser.get(link)

    button = browser.find_element_by_xpath("/html/body/form/div/div/button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_tag_name('span[id="input_value"]')
    x = x_element.text
    y = calc(x)
    print(y)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    button = browser.find_element_by_xpath('/html/body/form/div/div/button').click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()