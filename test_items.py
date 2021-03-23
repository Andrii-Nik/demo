link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button(browser):
    browser.get(link)
    button = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button")
    assert button in link



