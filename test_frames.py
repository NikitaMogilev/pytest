import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkbox(browser):
    chrome = browser
    url = 'http://the-internet.herokuapp.com/iframe'
    chrome.get(url)
    frame_locator = (By.XPATH, "//iframe[@title='Rich Text Area']")
    WebDriverWait(chrome, 10).until(EC.frame_to_be_available_and_switch_to_it(frame_locator))
    message_locator = (By.CSS_SELECTOR, "#tinymce p")
    message = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(message_locator)).text
    assert message == 'Your content goes here.'
