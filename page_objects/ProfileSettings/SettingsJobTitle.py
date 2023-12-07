from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from page_objects.BasePage import Basepage
from page_objects.Locators import SettingsJobTitleLocators


class SettingsJobTitle(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = SettingsJobTitleLocators()

    def clickJobTitleTab(self):
        self.element_click("job_title_tab_xpath", self.locators.job_title_tab_xpath)

    def clickClientJobTitle(self):
        self.element_click("client_job_title_btn_xpath", self.locators.client_job_title_btn_xpath)

    def enterName(self, JobName):
        self.enter_input_name(JobName, "enter_name_xpath", self.locators.enter_name_xpath)

    def clickCreateBtn(self):
        self.element_click("create_btn_xpath", self.locators.create_btn_xpath)

    def searchByName(self, JobSearchByName):
        self.enter_input_name(JobSearchByName, "search_by_name_xpath", self.locators.search_by_name_xpath)

    def clickJobEditBtn(self):
        self.element_click("job_edit_btn_xpath", self.locators.job_edit_btn_xpath)

    def jobNameUpdate(self):
        self.element_click("job_name_update_xpath", self.locators.job_name_update_xpath)

    def clickUpdateBtn(self):
        self.element_click("update_btn_xpath", self.locators.update_btn_xpath)

    def clickDeleteBtn(self):
        self.element_click("job_delete_btn_xpath", self.locators.job_delete_btn_xpath)

    def clickYesBtn(self):
        self.element_click("delete_yes_btn_xpath", self.locators.delete_yes_btn_xpath)

    def clickPinClient(self):
        self.element_click("pin_job_title_xpath", self.locators.pin_job_title_xpath)

    def clickUnPinClient(self):
        self.element_click("unpin_job_title_xpath", self.locators.unpin_job_title_xpath)

    def clickPageSelector(self):
        self.element_click("page_selector_xpath", self.locators.page_selector_xpath)

    def clickPageSelect(self):
        self.element_click("page_selector_10_xpath", self.locators.page_selector_10_xpath)

