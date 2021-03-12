import time
from selenium import webdriver

browser = webdriver.Chrome("C:\\Users\\asdfg\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver\\chromedriver.exe")

browser.get("https://www.youtube.com/?gl=UA&hl=ru")

xpath = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/paper-button/yt-icon'
button = browser.find_element_by_xpath(xpath).click()

input_email_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
browser.find_element_by_xpath(input_email_xpath).send_keys('emailTestForm@gmail.com')

put_but_afterEmail = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]'
browser.find_element_by_xpath(put_but_afterEmail).click()

time.sleep(10)
browser.refresh()

time.sleep(5)
browser.quit()

