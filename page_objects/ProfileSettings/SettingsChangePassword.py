from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from page_objects.BasePage import Basepage
from page_objects.Locators import SettingsChangePasswordLocators


class SettingsChangePassword(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = SettingsChangePasswordLocators()

    def clickPswChange(self):
        self.element_click("psw_change_xpath", self.locators.psw_change_xpath)

    def enterCurrentPsw(self, currentPsw):
        self.enter_input_name(currentPsw, "current_psw_xpath", self.locators.current_psw_xpath)

    def clickView(self):
        self.element_click("view_xpath", self.locators.view_xpath)

    def clickHide(self):
        self.element_click("hide_xpath", self.locators.hide_xpath)

    def enterNewPsw(self, newPsw):
        self.enter_input_name(newPsw, "new_psw_xpath", self.locators.new_psw_xpath)

    def enterConfirmPsw(self, confirmPsw):
        self.enter_input_name(confirmPsw, "confirm_psw_xpath", self.locators.confirm_psw_xpath)

    def updateBtn(self):
        self.element_click("updateBtn_xpath", self.locators.updateBtn_xpath)

