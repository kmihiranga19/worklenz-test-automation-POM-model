from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from page_objects.BasePage import Basepage
from page_objects.Locators import SettingsLabelsLocators


class SettingsLabels(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = SettingsLabelsLocators()

    def clickLabelTab(self):
        self.element_click("label_tab_xpath", self.locators.label_tab_xpath)

    def labelSearch(self, labelSearchName):
        self.enter_search_filed(labelSearchName, "label_search_xpath", self.locators.label_search_xpath)

    def clickPinClient(self):
        self.element_click("pin_labelTab_xpath", self.locators.pin_labelTab_xpath)

    def clickUnPinClient(self):
        self.element_click("unpin_labelTab_xpath", self.locators.unpin_labelTab_xpath)
