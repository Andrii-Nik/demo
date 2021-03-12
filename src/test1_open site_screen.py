import time
from selenium import webdriver

browser = webdriver.Chrome("C:\\Users\\asdfg\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver\\chromedriver.exe")

option = webdriver.ChromeOptions()
option.set_preference('dom.webnotifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')

browser = webdriver.Chrome(options=option)
browser.get('https://www.wikipedia.org/')
