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
# from locat import MainPageLocators
from locat import MainPageLocators




class ShopMainPage(BasePage):

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'http://automationpractice.pl/index.php'

    def click_chart(self):
        self.click_element(MainPageLocators.chart)

    def check_mainpage_logo(self):
        logo_address = self.get_atr(MainPageLocators.logo, 'src')
        assert logo_address == "http://automationpractice.pl/img/logo.jpg"

    def click_sigh_in(self):
        self.click_element(MainPageLocators.sigh_in)

    def click_women_button(self):
        self.click_element(MainPageLocators.women_button)