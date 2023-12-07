from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from page_objects.BasePage import Basepage
from page_objects.Locators import ReportingMembersLocators
from selenium.webdriver.common.action_chains import ActionChains


class Members(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = ReportingMembersLocators()

    def clickReportingTab(self):
        self.element_click("reporting_tab_xpath", self.locators.reporting_tab_xpath)

    def clickMembersTab(self):
        self.element_click("members_tab_xpath", self.locators.members_tab_xpath)

    def clickArchiveProject(self):
        self.element_click("include_archived_project_xpath", self.locators.include_archived_project_xpath)

    def clickTimeRangeLastWeekBtn(self):
        self.element_click("time_range_last_week_btn_xpath", self.locators.time_range_last_week_btn_xpath)

    def clickTimeRangeYesterdayBtn(self):
        self.element_click("time_range_yesterday_btn_xpath", self.locators.time_range_yesterday_btn_xpath)

    def clickTimeRangeLastMonthBtn(self):
        self.element_click("time_range_lastMonth_btn_xpath", self.locators.time_range_lastMonth_btn_xpath)

    def clickTimeRangeQuarterBtn(self):
        self.element_click("time_range_lastQuarter_btn_xpath", self.locators.time_range_quarter_btn_xpath)

    def clickTimeRangeYesterday(self):
        self.element_click("time_range_yesterday_xpath", self.locators.time_range_yesterday_xpath)

    def clickTimeRangeLastWeek(self):
        self.element_click("time_range_lastWeek_xpath", self.locators.time_range_lastWeek_xpath)

    def clickTimeRangeLastMonth(self):
        self.element_click("time_range_lastMonth_xpath", self.locators.time_range_lastMonth_xpath)

    def clickTimeRangeLastQuarter(self):
        self.element_click("time_range_lastQuarter_xpath", self.locators.time_range_lastQuarter_xpath)

