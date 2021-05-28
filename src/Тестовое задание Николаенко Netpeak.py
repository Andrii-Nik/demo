from selenium import webdriver
import time
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.color import Color

try:
    link = "https://netpeak.ua/"
    browser = webdriver.Chrome("C:\\Users\\asdfg\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver\\chromedriver.exe")
    browser.get(link)

    browser.implicitly_wait(5)

    buttonCareer = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[1]/div/nav/div[1]/div[1]/ul/li[4]")
    buttonCareer.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    buttonAnketa = browser.find_element_by_xpath("/html/body/header/div[2]/div/div/div[1]/a")
    buttonAnketa.click()

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.png"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_xpath("/html/body/input")
    element.send_keys(file_path)
    time.sleep(8)

    message = browser.find_element_by_xpath("/html/body/form/div[1]/div/div[1]/div[8]/div[2]/label")
    assert message.text == "Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf)."

    inputName = browser.find_element_by_id('inputName')
    inputName.send_keys("Ivan")
    inputLastname = browser.find_element_by_id('inputLastname')
    inputLastname.send_keys("Ivanov")
    inputEmail = browser.find_element_by_id('inputEmail')
    inputEmail.send_keys("test@gmail.com")
    inputPhone = browser.find_element_by_id('inputPhone')
    inputPhone.send_keys("+38000000000")
    selectYear = Select(browser.find_element_by_xpath("/html/body/form/div[1]/div/div[1]/div[11]/div[2]/select"))
    selectYear.select_by_index(1)
    selectMon = Select(browser.find_element_by_xpath("/html/body/form/div[1]/div/div[1]/div[11]/div[3]/select"))
    selectMon.select_by_index(1)
    selectDate = Select(browser.find_element_by_xpath("/html/body/form/div[1]/div/div[1]/div[11]/div[4]/select"))
    selectDate.select_by_index(1)

    buttonSendAnk = browser.find_element_by_id("submit")
    buttonSendAnk.click()

    RED = Color.from_string('red')
    messageRed = Color.from_string(browser.find_element_by_xpath("/html/body/div[2]/div/p").value_of_css_property('color'))
    assert messageRed == RED

    buttonCourse = browser.find_element_by_xpath("/html/body/header/div[2]/div/div/div[2]/div/nav/ul/li[4]/a")
    buttonCourse.click()

    check_url = browser.current_url
    assert check_url == "https://school.netpeak.group/"


finally:
    time.sleep(8)
    browser.quit()