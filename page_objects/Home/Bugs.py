from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from page_objects.BasePage import Basepage
from page_objects.Locators import BugsLocators


# Project group change(phase or priority) then try to create tasks and subtasks from home
class ChangeProjectGroup(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = BugsLocators()

    def clickProjectTab(self):
        self.element_click("project_Tab_xpath", self.locators.project_Tab_xpath)

    def select_project(self):
        self.element_click("project_select_xpath", self.locators.project_select_xpath)

    def clickProjectGroup(self):
        self.element_click("project_group_By", self.locators.project_group_By)

    def selectPhase(self):
        self.element_click("phase_xpath", self.locators.phase_xpath)

    def clickHome(self):
        self.element_click("home_xpath", self.locators.home_xpath)

    def enterTask(self, newTask):
        self.home_enter_task(newTask,"task_input_xpath", self.locators.task_input_xpath)

    def selectDueDate(self):
        self.element_click("select_today_xpath", self.locators.select_today_xpath)

    def selectProject(self):
        self.element_click("select_project_xpath", self.locators.select_project_xpath)

    def clickOpenTask(self):
        actions = ActionChains(self.browser)
        task = self.browser.find_element(By.XPATH, self.locators.task_xpath)
        actions.move_to_element(task).perform()
        time.sleep(2)
        self.browser.find_element(By.XPATH, self.locators.open_task_xpath).click()

    def clickSubTask(self):
        self.element_click("subTask_xpath", self.locators.subTask_xpath)

    def enterSubtask(self, subTask):
        self.enter_subTask(subTask, "enter_subtask_xpath", self.locators.enter_subtask_xpath)
