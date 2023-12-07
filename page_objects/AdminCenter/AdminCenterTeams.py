from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects.BasePage import Basepage
from page_objects.Locators import AdminCenterTeamsLocators


class AdminCenterTeams(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = AdminCenterTeamsLocators()

    def clickTeamBtn(self):
        self.element_click("teams_btn_xpath", self.locators.teams_btn_xpath)

    def clickRefreshBtn(self):
        self.element_click("refresh_btn_xpath", self.locators.refresh_btn_xpath)

    def clickAddTeamBtn(self):
        self.element_click("add_team_xpath", self.locators.add_team_xpath)

    def enterTeamName(self, teamName):
        self.enter_input_name(teamName, "team_name_xpath", self.locators.team_name_xpath)

    def createBtn(self):
        self.element_click("create_btn_xpath", self.locators.create_btn_xpath)

    def searchByName(self, searchTName):
        self.enter_search_filed(searchTName, "search_xpath", self.locators.search_xpath)

    def clickPageSelector(self):
        self.element_click("page_selector_xpath", self.locators.page_selector_xpath)

    def click5Page(self):
        self.element_click("page_5_xpath", self.locators.page_5_xpath)
