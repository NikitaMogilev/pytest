import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .base_page import random_name_address
from .base_page import BasePage
from .locat import CartLocators
from .locat import LoginPagelocators
from selenium.webdriver.support.select import Select




class ShopCartPage(BasePage):

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        # self.url = 'http://automationpractice.pl/index.php'
        # self.name_address = ''

    def check_cart_page(self):
        title = self.check_title()
        assert title == 'Order - My Store'

    def check_empty_cart(self):
        empty_cart = self.find_element(CartLocators.empty_cart)
        assert empty_cart

    def click_add_to_chart_dress(self):
        self.click_element(CartLocators.list_of_produkts)
        self.click_element(CartLocators.dress_add_to_cart)

    def go_to_chart_to_proceed_1(self):
        self.click_element(CartLocators.proceed_to_check_out_1)

    def increase_dress_quantity(self):
        self.click_element(CartLocators.quantity_increase)

    def decrease_dress_quantity(self):
        self.click_element(CartLocators.quantity_decrease)

    def total_price_calc(self):
        price_per_pcs = self.get_text_from_element(CartLocators.unit_price)
        price_per_pcs_1 = eval(price_per_pcs[1:])
        quanitity_pcs = self.get_atr(CartLocators.quantity, 'value')
        quanitity_pcs_1 = int(quanitity_pcs)
        shipping_price = self.get_text_from_element(CartLocators.shipping)
        shipping_price = eval(shipping_price[1:])
        tax_price = self.get_text_from_element(CartLocators.tax)
        tax_price_1 = eval(tax_price[1:])
        total_price_calc = pytest.approx((price_per_pcs_1 * quanitity_pcs_1 + shipping_price + tax_price_1), abs=1e-2)
        total_price_shown = self.get_text_from_element(CartLocators.total_price)
        assert total_price_calc == eval(total_price_shown[1:])

    def new_address_input(self):
        self.click_element(CartLocators.new_address)

    def go_to_chart_to_proceed_2(self):
        self.click_element(CartLocators.proceed_to_check_out_2)

    def user_verification(self):
        self.send_keys(locator=LoginPagelocators.verificated_user_email, content='nikita3@mail.ru')
        self.send_keys(locator=LoginPagelocators.verificated_user_password, content='qwerty')
        self.click_element(LoginPagelocators.sign_in_verificated_user)
        verify_user_name = self.get_text_from_element(LoginPagelocators.verify_user_logo)
        assert verify_user_name == 'Nikita Nikitin'

    def adress_pull(self):
        self.name_address = random_name_address(self)
        self.send_keys(locator=CartLocators.address, content="lenina 33")
        self.send_keys(locator=CartLocators.city, content="Tehas")
        self.selector(locator=CartLocators.state, value="50")
        self.send_keys(locator=CartLocators.zip_code, content="12345")
        self.send_keys(locator=CartLocators.home_phone, content="12345678")
        self.send_keys(locator=CartLocators.mobile_phone, content="12344444")
        self.send_keys(locator=CartLocators.edit_new_address, content=self.name_address)
        self.click_element(CartLocators.save_button)

    def go_to_chart_to_proceed_3(self):
        self.click_element(CartLocators.proceed_to_check_out_3)

    def go_to_chart_to_proceed_4_delivery(self):
        checkbox = self.find_element(CartLocators.terms_and_delivery_confirmation)
        checkbox.click()
        self.click_element(CartLocators.proceed_to_check_out_4)

    def type_pay_card(self):
        self.click_element(CartLocators.type_pay_card)

    def type_pay_check(self):
        self.click_element(CartLocators.type_pay_check)

    def confirm_order(self):
        self.click_element(CartLocators.confirm_order_button)
