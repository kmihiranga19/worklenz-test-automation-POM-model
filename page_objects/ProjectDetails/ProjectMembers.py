from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects.BasePage import Basepage
from page_objects.Locators import ProjectMembersLocators


class ProjectMembers(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = ProjectMembersLocators()

    def clickProjectTab(self):
        self.element_click("project_tab_xpath", self.locators.project_tab_xpath)

    def selectProject(self):
        self.element_click("select_project_xpath", self.locators.select_project_xpath)

    def clickMembers(self):
        self.element_click("members_xpath", self.locators.members_xpath)

    def clickRefreshBtn(self):
        self.element_click("refresh_btn_xpath", self.locators.refresh_btn_xpath)

    def clickRemoveBtn(self):
        self.element_click("remove_member_xpath", self.locators.remove_member_xpath)

    def clickOkBtn(self):
        self.element_click("ok_btn_xpath", self.locators.ok_btn_xpath)

    def clickPageSelector(self):
        self.element_click("page_selector_xpath", self.locators.page_selector_xpath)

    def select5Page(self):
        self.element_click("pages5_select_xpath", self.locators.pages5_select_xpath)

