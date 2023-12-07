from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from page_objects.BasePage import Basepage
from page_objects.Locators import WorkloadLocators


class Workload(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = WorkloadLocators()

    def clickProjectTab(self):
        self.element_click("project_tab_xpath", self.locators.project_tab_xpath)

    def selectProject(self):
        self.element_click("select_project_xpath", self.locators.select_project_xpath)

    def clickWorkloadTab(self):
        self.element_click("workload_tab_xpath", self.locators.workload_tab_xpath)

    def clickCreateTaskBtn(self):
        self.element_click("create_task_btn_xpath", self.locators.create_task_btn_xpath)

    def enterTaskName(self, taskName):
        self.enter_input_name(taskName, "enter_task_title_xpath", self.locators.enter_task_title_xpath)

    def clickAssigner(self):
        self.element_click("assigner_xpath", self.locators.assigner_xpath)

    def selectAssigner(self):
        self.element_click("select_assigner_xpath", self.locators.select_assigner_xpath)

    def clickTemporaryClick(self):
        self.element_click("temporary_click_xpath", self.locators.temporary_click_xpath)

    def clickShowStartDate(self):
        self.element_click(" show_startDate_xpath", self.locators.show_startDate_xpath)

    def clickStartDate(self):
        self.element_click("click_startDate_xpath", self.locators.click_startDate_xpath)

    def selectStartDate(self):
        self.element_click("select_startDate_xpath", self.locators.select_startDate_xpath)

    def clickEndDate(self):
        self.element_click("click_endDate_xpath", self.locators.click_endDate_xpath)

    def selectEndDate(self):
        self.element_click("select_endDate_xpath", self.locators.select_endDate_xpath)

    def setHours(self, hours):
        self.enter_input_name(hours, "Set_hour_xpath", self.locators.Set_hour_xpath)

    def clickDrawerClose(self):
        self.element_click(" drawer_close_btn_xpath", self.locators.drawer_close_btn_xpath)

    def clickExpandBtn(self):
        self.element_click("Expand_all_xpath", self.locators.Expand_all_xpath)

    def OpenAssignedTask(self):
        self.element_click("Assigned_task_open_xpath", self.locators.Assigned_task_open_xpath)

    def clickAddSubTask(self):
        self.element_click("click_subTask_xpath", self.locators.click_subTask_xpath)

    def enterSubtask(self, subtaskName):
        self.enter_subTask(subtaskName, "enter_subTask_xpath", self.locators.enter_subTask_xpath)

    def openSubTask(self):
        self.element_click("subtask_open_xpath", self.locators.subtask_open_xpath)

    def selectSubTaskAssigner(self):
        self.element_click("select_subTask_assigner_xpath", self.locators.select_subTask_assigner_xpath)

    def closeSubTask(self):
        self.element_click("back_btn_subTask_xpath", self.locators.back_btn_subTask_xpath)


