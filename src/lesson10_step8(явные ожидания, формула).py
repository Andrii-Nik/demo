from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math



try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome("C:\\Users\\asdfg\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver\\chromedriver.exe")
    browser.get(link)
    button = browser.find_element_by_id('book')
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    button.click()

    browser.execute_script("window.scrollBy(0, 300);")


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
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

