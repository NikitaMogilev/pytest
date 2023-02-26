import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import fixture
from time import sleep
from bs4 import BeautifulSoup


@fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_web(browser):
    chrome = browser
    chrome.maximize_window()
    url = 'http://thedemosite.co.uk/savedata.php'
    chrome.get(url=url)
    user_locator = (By.XPATH, "/html//form//td//tbody//input[contains(@name,'username')]")
    user_name = chrome.find_element(user_locator[0], user_locator[1])
    user_name.send_keys('fdgghgfhgf')
    password_locator = (By.XPATH, "/html//form//td//tbody//input[contains(@type,'password')]")
    password_box = chrome.find_element(password_locator[0], password_locator[1])
    password_box.send_keys('dfgdfg')
    save_button_locator = (By.XPATH, '//*[@value="save"]')
    save_button = chrome.find_element(save_button_locator[0], save_button_locator[1])
    save_button.click()
    chrome.close()


def test_web2(browser):
    chrome = browser
    chrome.maximize_window()
    chrome.implicitly_wait(10)
    chrome.get('https://demoqa.com/text-box')
    input_dict = {'Name': "nikita mogilev",
                 'Email': "nikita@mail.ru",
                 'Current Address ': "Saint-Petersburg, Pr. Prosvesheniya 86",
                 'Permananet Address ': "Saint-Petersburg, Pr. Prosvesheniya 84"
                 }
    locator_full_name = (By.XPATH, "/html/body//input[contains(@placeholder,'Full Name')]")
    locator_mail = (By.XPATH, "/html/body//input[contains(@placeholder,'name@example.com')]")
    Locator_cur_adress = (By.XPATH, "/html/body//textarea[contains(@placeholder,'Current Address')]")
    locator_perm_adress = (By.XPATH, "/html/body//textarea[contains(@id,'permanentAddress')]")
    locator_submit_button = (By.XPATH, "/html/body//button[contains(@id,'submit')]")
    name_box = chrome.find_element(locator_full_name[0], locator_full_name[1])
    name_box.send_keys(f"{input_dict.get('Name')}")
    Email_box = chrome.find_element(locator_mail[0], locator_mail[1])
    Email_box.send_keys(f'{input_dict.get("Email")}')
    adress_box1 = chrome.find_element(Locator_cur_adress[0], Locator_cur_adress[1])
    adress_box1.send_keys(f'{input_dict.get("Current Address ")}')
    adress_box2 = chrome.find_element(locator_perm_adress[0], locator_perm_adress[1])
    adress_box2.send_keys(f'{input_dict.get("Permananet Address ")}')
    button_box = chrome.find_element(locator_submit_button[0], locator_submit_button[1])
    chrome.execute_script("window.scrollTo(0, 1080)")
    time.sleep(10)
    button_box.click()
    output_box = chrome.find_elements(By.CLASS_NAME, 'mb-1')
    output_dict = {}
    for el in output_box:
        text = el.text
        key, value = text.split(':')
        output_dict[key] = value
    assert input_dict == output_dict
    chrome.close()
