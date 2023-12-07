from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects.BasePage import Basepage
from page_objects.Locators import ScheduleProjectLocators


class ScheduleProject(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = ScheduleProjectLocators

    def clickScheduleTab(self):
        self.element_click("schedule_tab_xpath", self.locators.schedule_tab_xpath)

    def clickProjectDropdown(self):
        self.element_click("project_dropdown_xpath", self.locators.project_dropdown_xpath)

    def clickWeekSelector(self):
        self.element_click("week_selector_xpath", self.locators.week_selector_xpath)

    def clickWeekPick(self):
        self.element_click("week_pick_xpath", self.locators.week_pick_xpath)

    def clickTimePeriod(self):
        self.element_click("time_period_xpath", self.locators.time_period_xpath)

    def clickTask(self):
        self.element_click("task_click_xpath", self.locators.task_click_xpath)

    def clickCloseBtn(self):
        self.element_click("close_btn_xpath", self.locators.close_btn_xpath)

    def clickCloseBtn2(self):
        self.element_click("close_btn2_xpath", self.locators.close_btn2_xpath)