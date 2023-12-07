from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects.BasePage import Basepage
from page_objects.Locators import ProjectWorkloadLocators


class ProjectWorkload(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = ProjectWorkloadLocators()

    def clickProjectTab(self):
        self.element_click("project_tab_xpath", self.locators.project_tab_xpath)

    def selectProject(self):
        self.element_click("select_project_xpath", self.locators.select_project_xpath)

    def clickCreateBtn(self):
        self.element_click(" create_task_btn_xpath", self.locators.create_task_btn_xpath)

    def enterTaskName(self, taskName):
        self.enter_input_name(taskName, "input_task_name_xpath", self.locators.input_task_name_xpath)

    def clickAssigner(self):
        self.element_click("assign_member_xpath", self.locators.assign_member_xpath)

    def selectAssignMember(self):
        self.element_click("select_member_xpath", self.locators.select_member_xpath)

    def clickTemp(self):
        self.element_click("temp_click_xpath", self.locators.temp_click_xpath)

    def drawerClose(self):
        self.element_click("drawer_close_xpath", self.locators.drawer_close_xpath)

    def clickWorkload(self):
        self.element_click("workload_tab_xpath", self.locators.workload_tab_xpath)

    def memberOpen(self):
        self.element_click("member_open_xpath", self.locators.member_open_xpath)

    def openTask(self):
        self.element_click("open_task_xpath", self.locators.open_task_xpath)

    def clickShowStartDate(self):
        self.element_click("show_start_date_xpath", self.locators.show_start_date_xpath)

    def clickStartDate(self):
        self.element_click("start_date_xpath", self.locators.start_date_xpath)

    def selectDate(self):
        self.element_click("select_start_date_xpath", self.locators.select_start_date_xpath)
