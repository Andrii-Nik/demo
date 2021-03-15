from selenium import webdriver
import time
import math
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome("C:\\Users\\asdfg\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver\\chromedriver.exe")
    browser.get(link)

    with open("test.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file
    input1 = browser.find_element_by_xpath('/html/body/div[1]/form/div/input[1]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('/html/body/div[1]/form/div/input[2]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('/html/body/div[1]/form/div/input[3]')
    input3.send_keys("Smolensk@ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_id('file')
    element.send_keys(file_path)

    button = browser.find_element_by_xpath("/html/body/div[1]/form/button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()