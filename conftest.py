import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome("C:\\Users\\asdfg\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver\\chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': es})
    browser = webdriver.Chrome(options=options)


