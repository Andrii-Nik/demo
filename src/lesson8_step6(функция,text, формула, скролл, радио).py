from selenium import webdriver
import time
import math

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome("C:\\Users\\asdfg\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver\\chromedriver.exe")
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_tag_name('span[id="input_value"]')
    x = x_element.text
    y = calc(x)
    print(y)

    browser.execute_script("window.scrollBy(0, 100);")

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    input2 = browser.find_element_by_id('robotCheckbox')
    input2.click()
    input3 = browser.find_element_by_id('robotsRule')
    input3.click()
    input4 = browser.find_element_by_class_name('btn.btn-primary')
    input4.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()