from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from page_objects.BasePage import Basepage
from page_objects.Locators import SettingsClientsLocators


class SettingsClients(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = SettingsClientsLocators()

    def clickClientTab(self):
        self.element_click("client_tab_xpath", self.locators.client_tab_xpath)

    def clickCreateBtn(self):
        self.element_click("create_client_btn_xpath", self.locators.create_client_btn_xpath)

    def enterName(self, name):
        self.enter_input_name(name, "enter_name_xpath", self.locators.enter_name_xpath)

    def createButton(self):
        self.element_click("create_button_xpath", self.locators.create_button_xpath)

    def searchByName(self, searchName):
        self.enter_search_filed(searchName, "search_by_name_xpath", self.locators.search_by_name_xpath)

    def clientNameEditBtn(self):
        self.element_click("client_edit_btn_xpath", self.locators.client_edit_btn_xpath)

    def clientNameUpdateBtn(self, updateName):
        self.enter_input_name(updateName, "client_name_update_xpath", self.locators.client_name_update_xpath)

    def clickUpdateBtn(self):
        self.element_click("update_btn_xpath", self.locators.update_btn_xpath)

    def clickDeleteBtn(self):
        self.element_click("client_delete_btn_xpath", self.locators.client_delete_btn_xpath)

    def clickDeleteYesBtn(self):
        self.element_click("delete_yes_btn_xpath", self.locators.delete_yes_btn_xpath)

    def clickPinClient(self):
        self.element_click("pin_client_xpath", self.locators.pin_client_xpath)

    def clickUnPinClient(self):
        self.element_click("unpin_xpath", self.locators.unpin_xpath)

    def clickPageSelector(self):
        self.element_click("page_selector_xpath", self.locators.page_selector_xpath)

    def clickPageSelect(self):
        self.element_click("page_selector_10_xpath", self.locators.page_selector_10_xpath)
