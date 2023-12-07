from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from page_objects.BasePage import Basepage
from page_objects.Locators import SettingsTeamMemberLocators


class SettingsTeamMember(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = SettingsTeamMemberLocators()

    def clickTeamMemberTab(self):
        self.element_click("team_members_tab_xpath", self.locators.team_members_tab_xpath)

    def clickRefreshBtn(self):
        self.element_click("refresh_btn_xpath", self.locators.refresh_btn_xpath)

    def searchMember(self, searchMemberName):
        self.enter_search_filed(searchMemberName, "search_input_xpath", self.locators.search_input_xpath)

    def clickAddMemberBtn(self):
        self.element_click("add_member_btn_xpath", self.locators.add_member_btn_xpath)

    def enterEmail(self, inviteEmail):
        self.enter_input_name(inviteEmail, "add_member_btn_xpath", self.locators.add_member_btn_xpath)

    def clickMemberEdit(self):
        self.element_click("member_edit_xpath", self.locators.member_edit_xpath)

    def clickJobTitle(self):
        self.element_click("job_title_xpath", self.locators.job_title_xpath)

    def selectTitle(self):
        self.element_click("select_title_xpath", self.locators.select_title_xpath)

    def clickAccess(self):
        self.element_click("access_xpath", self.locators.access_xpath)

    def selectAccess(self):
        self.element_click("member_xpath", self.locators.member_xpath)

    def clickUpdateBtn(self):
        self.element_click("update_btn_xpath", self.locators.update_btn_xpath)

    def clickDeleteBtn(self):
        self.element_click("delete_btn_xpath", self.locators.delete_btn_xpath)

    def clickDeleteYesBtn(self):
        self.element_click("yes_btn_xpath", self.locators.yes_btn_xpath)

    def clickPageSelector(self):
        self.element_click("page_selector_xpath", self.locators.page_selector_xpath)

    def clickPageSelect(self):
        self.element_click("page_selector_10_xpath", self.locators.page_selector_10_xpath)
