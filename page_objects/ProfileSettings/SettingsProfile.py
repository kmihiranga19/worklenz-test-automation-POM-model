from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from page_objects.BasePage import Basepage
from page_objects.Locators import SettingsProfileLocators


class SettingsProfile(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = SettingsProfileLocators()

    def clickProfileIcon(self):
        self.element_click("profile_icon_xpath", self.locators.profile_icon_xpath)

    def clickSettings(self):
        self.element_click("settings_xpath", self.locators.settings_xpath)

    def selectImage(self):
        self.element_click("upload_xpath", self.locators.upload_xpath)
        time.sleep(3)
        # Set the file path of the AutoIT script
        autoit_script = "C:\\Users\\Ceydigital\\Desktop\\pngtree.jpg"
        time.sleep(1)
        pyautogui.typewrite(autoit_script)
        pyautogui.press("enter")

    def enterName(self, name):
        self.enter_input_name(name, "name_xpath", self.locators.name_xpath)

    def saveBtn(self):
        self.element_click("save_btn_xpath", self.locators.save_btn_xpath)


