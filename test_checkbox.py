import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def test_checkbox(browser):
    chrome = browser
    url = 'http://the-internet.herokuapp.com/dynamic_controls'
    chrome.get(url)
    checkbox_locator = (By.XPATH, "//form[@id='checkbox-example']//input[@type='checkbox']")
    remove_but_locator = (By.XPATH, "//form[@id='checkbox-example']//button[@type='button']")
    remove_but = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable(remove_but_locator))
    remove_but.click()
    its_gone_locator = (By.XPATH, "//form[@id='checkbox-example']//p[@id='message']")
    its_gone = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(its_gone_locator))
    checkbox = WebDriverWait(chrome, 10).until_not(EC.presence_of_element_located(checkbox_locator))
    assert checkbox and its_gone
    input_box_locator = (By.XPATH, "//form[@id='input-example']/input[@type='text']")
    input_box = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(input_box_locator)).is_enabled()
    assert input_box == False
    enable_but_locator = (By.XPATH, "//form[@id='input-example']/button[@type='button']")
    enable_but = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable(enable_but_locator))
    enable_but.click()
    its_enable_locator = (By.XPATH, "//form[@id='input-example']/p[@id='message']")
    its_enable = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(its_enable_locator))
    input_box = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(input_box_locator)).is_enabled()
    assert input_box
