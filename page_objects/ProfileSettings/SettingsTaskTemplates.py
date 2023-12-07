from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from page_objects.BasePage import Basepage
from page_objects.Locators import SettingsTaskTemplatesLocators


class SettingsTaskTemplates(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = SettingsTaskTemplatesLocators()

    def clickTaskTemp(self):
        self.element_click("tasks_template_tab_xpath", self.locators.tasks_template_tab_xpath)
