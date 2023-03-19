from selenium.webdriver.common.by import By


def test_clicker(browser):
    chrome = browser
    chrome.maximize_window()
    chrome.implicitly_wait(15)
    url = 'https://ultimateqa.com/complicated-page/'
    chrome.get(url=url)
    button_xpath = chrome.find_element(By.XPATH, "//div[contains(@class, 'column_3')]//a[contains(@class,'button_4')]")
    button_xpath.click()
    button_css = chrome.find_element(By.CSS_SELECTOR, "div.et_pb_column_1_4 a.et_pb_button_4")
    button_css.click()
    button_class_name = chrome.find_element(By.CLASS_NAME, 'et_pb_button' and 'et_pb_button_4')
    button_class_name.click()
    chrome.close()