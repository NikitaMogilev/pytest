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
from base_page import BasePage
from locat import MainPageLocators
from locat import LoginPagelocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from base_page import random_mail


class ShopLoginPage(BasePage):

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.user_email = ''


    def check_login_page(self):
        title = self.check_title()
        assert title == 'Login - My Store'

    def new_user_email(self):
        self.click_element(LoginPagelocators.create_user_button)
        self.user_email = random_mail(self)
        self.send_keys(locator=LoginPagelocators.new_user_email, content=self.user_email)
        self.click_element(LoginPagelocators.create_user_button)


    def new_user_create_fail(self):
        self.send_keys(locator=LoginPagelocators.first_name, content='Nikita')
        self.send_keys(locator=LoginPagelocators.password, content='qwerty')
        self.click_element(LoginPagelocators.register_button)
        fail_alert = self.find_element(LoginPagelocators.fail_registration_alert)
        assert fail_alert.is_displayed()

    def new_user_create(self):
        radio_but = self.find_element(LoginPagelocators.mr_radio_button)
        radio_but.click()
        assert radio_but.is_selected()
        self.send_keys(locator=LoginPagelocators.first_name, content='Nikita')
        self.send_keys(locator=LoginPagelocators.last_name, content='Nikitin')
        assert self.get_atr(LoginPagelocators.email, 'value') == self.user_email
        self.send_keys(locator=LoginPagelocators.password, content='qwerty')
        self.selector(locator=LoginPagelocators.birth_bate_d, value='20')
        self.selector(LoginPagelocators.birth_bate_m, value='11')
        self.selector(locator=LoginPagelocators.birth_bate_y, value='2000')
        self.click_element(LoginPagelocators.register_button)
        try:
            pass
        except:
            self.accept_alert()
        registration_pass = self.find_element(LoginPagelocators.success_registration)
        assert registration_pass.is_displayed()

    def quit_account(self):
        self.click_element(LoginPagelocators.sign_out)

    def twice_user_created(self):
        self.user_email = 'nikita3@mail.ru'
        self.send_keys(locator=LoginPagelocators.new_user_email, content=self.user_email)
        self.click_element(LoginPagelocators.create_user_button)
        assert self.find_element(LoginPagelocators.twice_user).is_displayed()

    def user_verification(self):
        self.send_keys(locator=LoginPagelocators.verificated_user_email, content='nikita3@mail.ru')
        self.send_keys(locator=LoginPagelocators.verificated_user_password, content='qwerty')
        self.click_element(LoginPagelocators.sign_in_verificated_user)
        verify_user_name = self.get_text_from_element(LoginPagelocators.verify_user_logo)
        assert verify_user_name == 'Nikita Nikitin'
