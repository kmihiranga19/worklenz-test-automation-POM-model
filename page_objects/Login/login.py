from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.BasePage import Basepage
from page_objects.Locators import LoginLocators


class Login(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = LoginLocators()

    def clickLogin(self):
        self.element_click("login_btn_xpath", self.locators.login_btn_xpath)

    def setEmail(self, email):
        self.enter_login_email(email,"email_input_xpath", self.locators.email_input_xpath)

    def setpassword(self, password):
        self.enter_login_password(password, "password_input_xpath", self.locators.password_input_xpath)

    def submit(self):
        self.element_click("login_submit_btn_xpath", self.locators.login_submit_btn_xpath)

