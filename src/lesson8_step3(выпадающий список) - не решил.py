from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome("C:\\Users\\asdfg\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver\\chromedriver.exe")
    browser.get(link)
    num_one = browser.find_element_by_tag_name('span[id="num1"]')
    x = num_one.text
    num_two = browser.find_element_by_tag_name('span[id="num2"]')
    y = num_two.text
    z = str(int(x) + int(y))
    print(z)
    select = Select(browser.find_element_by_id("dropdown").click())
    select.select_by_value(int(x) + int(y))
    button = browser.find_element_by_xpath('/html/body/div[1]/form/button/font/font')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()