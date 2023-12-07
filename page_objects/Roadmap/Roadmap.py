from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from page_objects.BasePage import Basepage
from page_objects.Locators import RoadmapLocators
from selenium.webdriver.common.action_chains import ActionChains


class Roadmap(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = RoadmapLocators()

    def clickProjectTab(self):
        self.element_click("project_tab_xpath", self.locators.project_tab_xpath)

    def selectProject(self):
        self.element_click("select_project_xpath", self.locators.select_project_xpath)

    def clickRoadmapTab(self):
        self.element_click("roadmap_tab_xpath", self.locators.Roadmap_tab_xpath)

    def clickAddTaskBtn(self):
        self.element_click("add_task_btn_xpath", self.locators.Add_task_btn_xpath)

    def enterTaskName(self, TaskName):
        self.enter_input_name(TaskName, "Task_title_input_xpath", self.locators.Task_title_input_xpath)

    def clickAssigner(self):
        self.element_click("assigner_xpath", self.locators.assigner_xpath)

    def selectAssigner(self):
        self.element_click("select_assigner_xpath", self.locators.select_assigner_xpath)

    def clickTemporaryClick(self):
        self.element_click("temporary_click_xpath", self.locators.temporary_click_xpath)

    def clickShowStartDate(self):
        self.element_click("show_startDate_xpath", self.locators.show_startDate_xpath)

    def clickStartDate(self):
        self.element_click("click_startDate_xpath", self.locators.click_startDate_xpath)

    def selectStartDate(self):
        self.element_click("select_startDate_xpath", self.locators.select_startDate_xpath)

    def clickEndDate(self):
        self.element_click("click_endDate_xpath", self.locators.click_endDate_xpath)

    def selectEndDate(self):
        self.element_click("select_endDate_xpath", self.locators.select_endDate_xpath)

    def clickHour(self):
        self.element_click("Set_hour_xpath", self.locators.Set_hour_xpath)

    def enterHour(self, estimatedHour):
        self.enter_input_name(estimatedHour, "Set_hour_xpath", self.locators.Set_hour_xpath)

    def clickAddSubTask(self):
        self.element_click("click_subTask_xpath", self.locators.click_subTask_xpath)

    def enterSubtask(self, subtaskName):
        self.enter_subTask(subtaskName, "enter_subTask_xpath", self.locators.enter_subTask_xpath)

    def openSubTask(self):
        self.element_click("subtask_open_xpath", self.locators.subtask_open_xpath)

    def selectEndDateToSubTask(self):
        self.element_click("select_endDate_subTask_xpath", self.locators.select_endDate_subTask_xpath)

    def clickBackBtn(self):
        self.element_click("back_btn_xpath", self.locators.back_btn_xpath)

    def clickDrawerClose(self):
        self.element_click("drawer_close_btn_xpath", self.locators.drawer_close_btn_xpath)

    def parentTaskRightClick(self):
        task_right_click = self.browser.find_element(By.XPATH, self.locators.parentTaskRightClick_xpath)
        actions = ActionChains(self.browser)
        actions.context_click(task_right_click).perform()

    def clickSubTaskAddBtn(self):
        self.element_click("parentTaskRightClick_addSubTask_xpath", self.locators.parentTaskRightClick_addSubTask_xpath)

    def clickExpandAllBtn(self):
        self.element_click("expand_all_xpath", self.locators.expand_all_xpath)

    def clickCollapseBtn(self):
        self.element_click("expand_all_xpath", self.locators.expand_all_xpath)

    def clickZoomInBtn(self):
        self.element_click("zoom_in_xpath", self.locators.zoom_in_xpath)

    def clickZoomOutBtn(self):
        self.element_click("zoom_out_xpath", self.locators.zoom_out_xpath)

    def clickZoomInFitBtn(self):
        self.element_click("zoom_in_fit_xpath", self.locators.zoom_in_fit_xpath)

    def clickShowPhase(self):
        self.element_click("show_phases_xpath", self.locators.show_phases_xpath)


