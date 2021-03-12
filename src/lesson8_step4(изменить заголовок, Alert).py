from selenium import webdriver

browser = webdriver.Chrome("C:\\Users\\asdfg\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver\\chromedriver.exe")
browser.execute_script("document.title='Script executing';alert('Robots at work');")
