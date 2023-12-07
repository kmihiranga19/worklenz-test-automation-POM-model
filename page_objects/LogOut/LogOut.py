from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects.BasePage import Basepage
from page_objects.Locators import LogOutLocators


class LogOut(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = LogOutLocators()

    def clickProfileIcon(self):
        self.element_click("profile_icon_xpath", self.locators.profile_icon_xpath)

    def clickLogOutBtn(self):
        self.element_click("log_out_btn_xpath", self.locators.log_out_btn_xpath)

    def clickCancelBtn(self):
        self.element_click("cancel_btn_xpath", self.locators.cancel_btn_xpath)

    def clickOkBtn(self):
        self.element_click("ok_btn_xpath", self.locators.ok_btn_xpath)
