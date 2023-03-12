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
from shop_main_page import ShopMainPage
from shop_cart_page import ShopCartPage
from shop_login_page import ShopLoginPage
from locat import MainPageLocators
from locat import LoginPagelocators
from locat import CartLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select


def test_fail_sigh_in(driver):
    main_page = ShopMainPage(driver)
    login_page = ShopLoginPage(driver)
    main_page.open()
    main_page.click_sigh_in()
    login_page.check_login_page()
    login_page.new_user_email()
    login_page.new_user_create_fail()


def test_sign_in(driver):
    main_page = ShopMainPage(driver)
    login_page = ShopLoginPage(driver)
    main_page.open()
    main_page.click_sigh_in()
    login_page.check_login_page()
    login_page.new_user_email()
    login_page.new_user_create()


def test_twice_registration_error(driver):
    main_page = ShopMainPage(driver)
    login_page = ShopLoginPage(driver)
    main_page.open()
    main_page.click_sigh_in()
    login_page.check_login_page()
    login_page.twice_user_created()


def test_vereficate_user_sign_in(driver):
    main_page = ShopMainPage(driver)
    login_page = ShopLoginPage(driver)
    main_page.open()
    main_page.click_sigh_in()
    login_page.user_verification()
    login_page.quit_account()


def test_main_logo(driver):
    main_page = ShopMainPage(driver)
    main_page.open()
    main_page.check_mainpage_logo()


def test_empty_cart(driver):
    main_page = ShopMainPage(driver)
    cart_page = ShopCartPage(driver)
    main_page.open()
    main_page.click_chart()
    cart_page.check_cart_page()
    cart_page.check_empty_cart()


def test_order(driver):
    main_page = ShopMainPage(driver)
    cart_page = ShopCartPage(driver)
    login_page = ShopLoginPage(driver)
    main_page.open()
    main_page.click_sigh_in()
    try:
        cart_page.user_verification()
    except:
        login_page.new_user_email()
        login_page.new_user_create()
    main_page.click_women_button()
    cart_page.click_add_to_chart_dress()
    cart_page.go_to_chart_to_proceed_1()
    cart_page.increase_dress_quantity()
    time.sleep(5)
    cart_page.total_price_calc()
    cart_page.go_to_chart_to_proceed_2()
    try:
        cart_page.adress_pull()
    except:
        cart_page.new_address_input()
        cart_page.adress_pull()
    cart_page.go_to_chart_to_proceed_3()
    cart_page.go_to_chart_to_proceed_4_delivery()
    cart_page.type_pay_check()
    cart_page.confirm_order()
