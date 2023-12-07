from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects.BasePage import Basepage
from page_objects.Locators import TeamSelectionLocators


class TeamSelection(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = TeamSelectionLocators()

    def clickTeamSelection(self):
        self.element_click("team_selection_xpath", self.locators.team_selection_xpath)

    def clickSelectTeam(self):
        self.element_click("select_team_xpath", self.locators.select_team_xpath)

    def clickTeamSelection2(self):
        self.element_click("team_selection2_xpath", self.locators.team_selection2_xpath)

    def clickSelectTeam2(self):
        self.element_click("select_team2_xpath", self.locators.select_team2_xpath)
