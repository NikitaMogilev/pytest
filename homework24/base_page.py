import time
import pytest
from retrying import retry
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from retrying import retry
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import random

def random_name_address(self):
    validchars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    add_char = ''
    adress_name = 'my address'
    loginlen = random.randint(1, 3)
    for i in range(loginlen):
        pos = random.randint(0, len(validchars) - 1)
        add_char += validchars[pos]
    addres = adress_name + add_char
    return addres


def random_mail(self):
    validchars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    login = ''
    server = '@mail.ru'
    loginlen = random.randint(5, 10)
    for i in range(loginlen):
        pos = random.randint(0, len(validchars) - 1)
        login = login + validchars[pos]
    email = login + server
    return email

class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.webdriver: webdriver.Chrome = driver
        driver.maximize_window()
        self.url = ''

    def open_url(self, url):
        self.webdriver.get(url)

    def open(self):
        self.open_url(url=self.url)


    def check_title(self):
        return self.webdriver.title

    def get_url(self):
        return self.webdriver.current_url

    def get_atr(self, locator: tuple, atr: str, timer=15):
        element = WebDriverWait(self.webdriver, timer).until(EC.presence_of_element_located(locator))
        return element.get_attribute(atr)

    def selector(self, locator: tuple, value: str, timer=10):
        element = WebDriverWait(self.webdriver, timer).until(EC.presence_of_element_located(locator))
        return Select(element).select_by_value(value)

    def find_element(self, locator: tuple, timer=10) -> WebElement:
        return WebDriverWait(self.webdriver, timer).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, timer=10):
        return WebDriverWait(self.webdriver, timer).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator: tuple, timer=10):
        return WebDriverWait(self.webdriver, timer).until(EC.element_to_be_clickable(locator)).click()

    def submit_element(self, locator: tuple, timer=10):
        return WebDriverWait(self.webdriver, timer).until(EC.element_to_be_clickable(locator)).submit()

    def send_keys(self, locator, content, timer=10):
        input_field = WebDriverWait(self.webdriver, timer).until(EC.element_to_be_clickable(locator))
        input_field.clear()
        input_field.send_keys(content)

    def get_text_from_element(self, locator, timer=10):
        element = self.find_element(locator, timer)
        return element.text

    def switch_to_iframe(self, iframe_locator, timer=10):
        WebDriverWait(self, timer).until(EC.frame_to_be_available_and_switch_to_it(iframe_locator))

    def switch_to_default_context(self):
        self.webdriver.switch_to.default_content()

    def accept_alert(self):
        alert_el = self.webdriver.switch_to.alert
        alert_el.accept()
        self.switch_to_default_context()

    def dismiss_alert(self):
        alert_el = self.webdriver.switch_to.alert
        alert_el.dismiss()
        self.switch_to_default_context()

    def fill_and_accept_alert(self, content):
        alert_el = self.webdriver.switch_to.alert
        alert_el.send_keys(content)
        alert_el.accept()
        self.switch_to_default_context()


    @retry(stop_max_delay=10000)
    def element_click_with_retry(self, locator, timer=30):
        return (
            WebDriverWait(self.webdriver, timer).until(
                EC.element_to_be_clickable(locator), message=f"Can't find element by locator {locator}"
            )
        ).click()

