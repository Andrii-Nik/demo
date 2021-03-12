from selenium import webdriver
import time

browser = webdriver.Chrome('C:\\Users\\asdfg\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver\\chromedriver.exe')
browser.get("http://suninjuly.github.io/wait1.html")

browser.implicitly_wait(5)

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text