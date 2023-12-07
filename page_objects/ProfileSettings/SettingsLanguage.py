from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from page_objects.BasePage import Basepage
from page_objects.Locators import SettingsLanguageLocators


class SettingsLanguage(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = SettingsLanguageLocators()

    def clickLanguageRegion(self):
        self.element_click("language_region_xpath", self.locators.language_region_xpath)

    def clickLanguageSelect(self):
        self.element_click("language_select_xpath", self.locators.language_select_xpath)

    def clickEnglish(self):
        self.element_click("english_xpath", self.locators.english_xpath)

    def clickTimeZone(self):
        self.element_click("time_zone_xpath", self.locators.time_zone_xpath)

    def selectTimeZone(self):
        self.element_click("select_time_zone_xpath", self.locators.select_time_zone_xpath)

    def saveBtn(self):
        self.element_click("save_btn_xpath", self.locators.save_btn_xpath)
