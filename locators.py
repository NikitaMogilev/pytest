from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import fixture


def test_locators(browser):
    chrome = browser
    chrome.maximize_window()
    chrome.implicitly_wait(10)
    url = 'https://baraholka.onliner.by/'
    chrome.get(url=url)
    start_title = browser.title
    locator_button_ad = (By.CSS_SELECTOR, 'a.b-btn-fleamarket__1[href="/fleamarketposting.php"]')
    button_ad = chrome.find_element(locator_button_ad[0], locator_button_ad[1])
    locator_q_video = (By.XPATH, "//a[@href='./viewforum.php?f=286'and text()='Видеокарты']/../sup")
    quantity_video = chrome.find_element(locator_q_video[0], locator_q_video[1])
    locator_q_dresses = (By.XPATH, "//a[@href='./viewforum.php?f=255' and text()='Платья']/../sup")
    quantity_dresses = chrome.find_element(locator_q_dresses[0], locator_q_dresses[1])
    button_ad.click()
    finish_title = browser.title
    assert start_title != finish_title
    chrome.close()
