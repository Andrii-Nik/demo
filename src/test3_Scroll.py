import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("C:\\Users\\asdfg\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver\\chromedriver.exe")

browser.get("https://www.youtube.com/?gl=UA&hl=ru")

html = browser.find_element_by_tag_name('html')

for i in range(30):
    html.send_keys(Keys.DOWN)


time.sleep(5)
browser.quit()

