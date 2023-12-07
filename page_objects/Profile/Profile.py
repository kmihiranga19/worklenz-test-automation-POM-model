from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.BasePage import Basepage
from page_objects.Locators import ProfileLocators


class Profile(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = ProfileLocators()

    def profile_icon(self):
        self.element_click("profile_icon_xpath", self.locators.profile_icon_xpath)

    def admin_center(self):
        self.element_click("admin_center_xpath", self.locators.admin_center_xpath)

    def profile_icon2(self):
        self.element_click("profile_icon2_xpath", self.locators.profile_icon2_xpath)

    def settings(self):
        self.element_click("settings_xpath", self.locators.settings_xpath)

    def profile_icon3(self):
        self.element_click("log_out_xpath", self.locators.log_out_xpath)

    def log_out(self):
        self.element_click("log_out_xpath", self.locators.log_out_xpath)

    def close(self):
        self.element_click("close_btn_xpath", self.locators.close_btn_xpath)

