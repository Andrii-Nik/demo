
from selenium import webdriver
import time


def test_abs1(self):
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome("C:\\Users\\asdfg\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver\\chromedriver.exe")
    browser.get(link)

    input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
    input1.send_keys('Ivan')
    input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
    input1.send_keys('Ivanov')
    input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
    input1.send_keys('Ivanovich')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
     welcome_text = welcome_text_elt.text

def test_abs2(self):
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome("C:\\Users\\asdfg\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver\\chromedriver.exe")
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
    input1.send_keys('Ivan')
    input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
    input1.send_keys('Ivanov')
    input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
    input1.send_keys('Ivanovich')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

