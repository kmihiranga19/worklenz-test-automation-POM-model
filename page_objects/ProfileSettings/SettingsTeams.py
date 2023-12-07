from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from page_objects.BasePage import Basepage
from page_objects.Locators import SettingsTeamsLocators


class SettingsTeams(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = SettingsTeamsLocators()

    def clickPin(self):
        self.element_click("pinTeamsTab_xpath", self.locators.pinTeamsTab_xpath)