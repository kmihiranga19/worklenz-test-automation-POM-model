from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects.BasePage import Basepage
from page_objects.Locators import AdminCenterUsersLocators


class AdminCenterUsers(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = AdminCenterUsersLocators()

    def clickUsersBtn(self):
        self.element_click("users_btn_xpath", self.locators.users_btn_xpath)

    def clickRefreshBtn(self):
        self.element_click("refresh_btn_xpath", self.locators.refresh_btn_xpath)

    def searchByName(self, searchName):
        self.enter_search_filed(searchName, "search_xpath", self.locators.search_xpath)

    def clickPageSelector(self):
        self.element_click("page_selector_xpath", self.locators.page_selector_xpath)

    def clickPage5(self):
        self.element_click("page5_xpath", self.locators.page5_xpath)
