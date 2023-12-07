from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects.BasePage import Basepage
from page_objects.Locators import AdminCenterOverviewLocators


class AdminCenterOverview(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = AdminCenterOverviewLocators()

    def clickProfileIcon(self):
        self.element_click("profile_icon_xpath", self.locators.profile_icon_xpath)

    def clickAdminBtn(self):
        self.element_click("admin_center_btn_xpath", self.locators.admin_center_btn_xpath)

    def organizationName(self):
        self.element_click("organization_name_xpath", self.locators.organization_name_xpath)

    def enterName(self, name):
        self.enter_admin_center_overview(name, "input_xpath", self.locators.input_xpath)

    def organizationOwner(self):
        self.element_click("organization_owner_xpath", self.locators.organization_owner_xpath)

    def organizationNo(self, number):
        self.enter_admin_center_overview(number, "input2_xpath", self.locators.input2_xpath)
