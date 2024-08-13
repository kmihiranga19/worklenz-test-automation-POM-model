from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from page_objects.BasePage import Basepage
from page_objects.Locators import WorkloadLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


class Workload(Basepage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
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

    def go_to_projects(self):
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//strong[normalize-space()='Projects']"))).click()
        time.sleep(10)

    def get_teams(self):
        switch_team = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "teams-switch")))
        switch_team.click()
        time.sleep(3)
        teams_list = self.driver.find_elements(By.CLASS_NAME, "team-list-item")
        time.sleep(3)
        return teams_list

    def workload_projects(self):
        t_body = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))
        t_body_wait = WebDriverWait(t_body, 10)
        projects = t_body_wait.until(EC.visibility_of_any_elements_located((By.TAG_NAME, "tr")))
        projects[0].click()  # select need project using index

    def show_need_fields(self):
        fields_toggle = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//button[@class='ant-btn ant-dropdown-trigger columns-toggle']")))
        fields_toggle.click()
        fields = self.wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, "ant-dropdown-menu-item")))
        label_class = fields[4].get_attribute("class")
        priority_class = fields[9].get_attribute("class")
        if "ant-checkbox-wrapper-checked" not in label_class and priority_class:
            fields[4].click()
            fields[9].click()
            fields_toggle.click()
        else:
            fields_toggle.click()

    def get_checked_members(self):
        membersA = []
        member_dropdown = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "members-dropdown")))
        members = member_dropdown.find_elements(By.TAG_NAME, "li")
        for member in members:
            member_class = member.get_attribute("class")
            if "ant-checkbox-wrapper-checked" in member_class:
                user_select = member.find_element(By.CLASS_NAME, "user-select-none")
                div = user_select.find_element(By.TAG_NAME, "div")
                member_name = div.find_element(By.TAG_NAME, "span").text
                membersA.append(member_name)
                time.sleep(1)

                # member_mail = member.find_element(By.TAG_NAME, "small").text
                # membersA.append(member_mail)

        return membersA

    def task_list(self):
        tasks_rows = self.wait.until(EC.visibility_of_any_elements_located((By.TAG_NAME, "worklenz-task-list-row")))
        filename = "_records11.csv"
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            fields = ['Member', 'Task_name', 'Start_date', 'End_date']
            csvwriter.writerow(fields)
            for task_row in tasks_rows:
                task_name = task_row.find_element(By.CLASS_NAME, "task-name-text").text
                start_date = task_row.find_element(By.TAG_NAME, "worklenz-task-list-start-date")
                start_date_input = start_date.find_element(By.TAG_NAME, "input")
                start_date_value = start_date_input.get_attribute("value")
                end_date = task_row.find_element(By.TAG_NAME, "worklenz-task-list-end-date")
                end_date_input = end_date.find_element(By.TAG_NAME, "input")
                end_date_value = end_date_input.get_attribute("value")
                task_row.find_element(By.TAG_NAME, "worklenz-task-list-members").click()
                members_list = self.get_checked_members()
                for member in members_list:
                    csvwriter.writerow([member, task_name, start_date_value, end_date_value])
                self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='OK']"))).click()
                time.sleep(2)

    def workload_main(self, teams):
        teams[0].click()  # select need team using team index
        time.sleep(2)
        self.workload_projects()
        self.show_need_fields()
        self.task_list()
