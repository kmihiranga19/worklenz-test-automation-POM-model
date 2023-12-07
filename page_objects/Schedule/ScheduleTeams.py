from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects.BasePage import Basepage
from page_objects.Locators import ScheduleTeamsLocators


class ScheduleTeams(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = ScheduleTeamsLocators()

    def clickScheduleTab(self):
        self.element_click("schedule_tab_xpath", self.locators.schedule_tab_xpath)

    def clickTeamsBtn(self):
        self.element_click("teams_btn_xpath", self.locators.teams_btn_xpath)

    def clickTeamsDropdown(self):
        self.element_click("teams_dropdown_xpath", self.locators.teams_dropdown_xpath)

    def clickTeamsDropdownClose(self):
        self.element_click("teams_dropdown_close_xpath", self.locators.teams_dropdown_close_xpath)

    def clickWeekSelector(self):
        self.element_click("week_selector_xpath", self.locators.week_selector_xpath)

    def clickPickDate(self):
        self.element_click("pick_date_xpath", self.locators.pick_date_xpath)

    def clickTimePeriod(self):
        self.element_click("time_period_xpath", self.locators.time_period_xpath)

    def clickTaskOpen(self):
        self.element_click("task_open_xpath", self.locators.task_open_xpath)

    def clickTaskClose(self):
        self.element_click("task_close_xpath", self.locators.task_close_xpath)

    def clickScheduleClose(self):
        self.element_click("schedule_close_xpath", self.locators.schedule_close_xpath)
