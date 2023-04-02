from random import randint
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
# from .base_page import BasePage
# from .shop_cart_page import ShopCartPage
# from .shop_login_page import ShopLoginPage
# from .shop_main_page import ShopMainPage
# from locat import MainPageLocators
# from locat import LoginPagelocators
# from locat import CartLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from pytest_bdd import scenarios, given, when, then, parsers
from locat import MainPageLocators
from locat import LoginPagelocators
from locat import CartLocators


def random_mail():
    validchars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    login = ''
    server = '@mail.ru'
    loginlen = randint(5, 10)
    for i in range(loginlen):
        pos = randint(0, len(validchars) - 1)
        login = login + validchars[pos]
    email = login + server
    return email


scenarios('../feature/sign_in.feature')


@given('Open page of internetshop')
def open_page(driver):
    url = 'http://automationpractice.pl/index.php'
    driver.get(url)


@when('Click on SIGN IN button')
def click_sign_in_but(driver):
    sign_in_but = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.sigh_in))
    sign_in_but.click()


@then('Check that we are in new page of registration')
def check_login_page(driver):
    title = driver.title
    assert title == 'Login - My Store'


@when('We are fill form of registration, like name, surname and other')
def send_new_email_and_user_fill_form(driver):
    new_user_but = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPagelocators.create_user_button))
    # new_user_but.click()
    input_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPagelocators.new_user_email))
    input_field.click()
    input_field.clear()
    user_email = random_mail()
    input_field.send_keys(user_email)
    new_user_but.click()

    radio_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPagelocators.mr_radio_button))
    radio_button.click()
    assert radio_button.is_selected()
    first_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPagelocators.first_name))
    first_name.send_keys('Nikita')

    last_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPagelocators.last_name))
    last_name.send_keys('Nikitin')

    email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPagelocators.email))
    assert email.get_attribute('value') == user_email

    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPagelocators.password))
    password.send_keys('qwerty12')

    Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPagelocators.birth_bate_d))).select_by_value('20')
    Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPagelocators.birth_bate_m))).select_by_value('10')
    Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPagelocators.birth_bate_y))).select_by_value('2000')

    reg_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPagelocators.register_button))
    reg_button.click()



@then('We wil see message of registration is comlete')
def registration_pass(driver):
    registration_ok = WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPagelocators.success_registration))
    print('dfgdg')
    assert registration_ok.is_displayed()
