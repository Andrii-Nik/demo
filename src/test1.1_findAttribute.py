import time
from selenium import webdriver

browser = webdriver.Chrome("C:\\Users\\asdfg\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver\\chromedriver.exe")
browser.get("https://www.youtube.com/?gl=UA&hl=ru")

block = browser.find_element_by_class_name('style-scope yt-img-shadow')
all_video = block.find_elements_by_tag_name('yt-img-shadow')

for video in all_video:
    print(video.get_attribute('class'))

#не работает))






