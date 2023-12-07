from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from page_objects.BasePage import Basepage
from page_objects.Locators import PhaseLocators


class phase(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = PhaseLocators()

    def clickProjectTab(self):
        self.element_click("project_tab_xpath", self.locators.project_tab_xpath)

    def selectProject(self):
        self.element_click("select_project_xpath", self.locators.select_project_xpath)

    def projectGroupBy(self):
        self.element_click("project_group_by_xpath", self.locators.project_group_by_xpath)

    def selectPhase(self):
        self.element_click("select_phase_xpath", self.locators.select_phase_xpath)

    def clickShowFiled(self):
        self.element_click("show_filed_xpath", self.locators.show_filed_xpath)

    def scroll_down(self):
        scroll_down = self.browser.find_element(By.CSS_SELECTOR, self.locators.scroll_down_xpath)
        self.browser.execute_script("arguments[0].scrollBy(0,0);", scroll_down)

    def selectPhaseFiled(self):
        self.element_click("select_phase_filed_xpath", self.locators.select_phase_filed_xpath)

    def clickPhaseSettings(self):
        self.element_click("phase_settings_xpath", self.locators.phase_settings_xpath)

    def enterPhaseLabel(self, phaseLabel):
        self.enter_input_name(phaseLabel, "phase_label_xpath", self.locators.phase_label_xpath)

    def clickAddPhaseOptionBtn(self):
        self.element_click("add_phase_option_xpath", self.locators.add_phase_option_xpath)

    def enterPhaseOption01(self, PhaseOption01):
        self.enter_input_name(PhaseOption01, "phase_option_01_xpath", self.locators.phase_option_01_xpath)

    def enterPhaseOption02(self, PhaseOption02):
        self.enter_input_name(PhaseOption02, "phase_option_02_xpath", self.locators.phase_option_02_xpath)

    def enterPhaseOption03(self, PhaseOption03):
        self.enter_input_name(PhaseOption03, "phase_option_03_xpath", self.locators.phase_option_03_xpath)

    def phaseOptionDelete(self):
        self.element_click("phase_option_delete_xpath", self.locators.phase_option_delete_xpath)

    def closeDrawer(self):
        self.element_click("close_drawer_xpath", self.locators.close_drawer_xpath)

    def clickPhaseMenu(self):
        self.element_click("phase_menu_xpath", self.locators.phase_menu_xpath)

    def clickRename(self):
        self.element_click("renameBtn_xpath", self.locators.renameBtn_xpath)

    def renamePhaseOption(self, renameTask):
        self.enter_renamePhase(renameTask, "renamePhase_xpath", self.locators.renamePhase_xpath)

    def clickUnmappedAddTask(self):
        self.element_click("unmapped_add_task_xpath", self.locators.unmapped_add_task_xpath)

    def enterUnmappedTask(self, taskName):
        self.enter_task(taskName, "unmapped_enter_task_xpath", self.locators.unmapped_enter_task_xpath)

    def clickPlaning(self):
        self.element_click(" planing_option_xpath", self.locators.planing_option_xpath)

    def clickAddPlaningTask(self):
        self.element_click("planing_option_add_task_xpath", self.locators.planing_option_add_task_xpath)

    def enterPlaningTask(self, taskName):
        self.enter_task(taskName, "planing_option_enter_task_xpath", self.locators.planing_option_enter_task_xpath)

    def taskRightClick(self):
        task_right_click = self.browser.find_element(By.XPATH, self.locators.task_right_click_xpath)
        actions = ActionChains(self.browser)
        actions.context_click(task_right_click).perform()

    def taskMoveTo(self):
        self.element_click("task_move_to_xpath", self.locators.task_move_to_xpath)

    def selectMovePhase(self):
        self.element_click("select_move_to_review_xpath", self.locators.select_move_to_review_xpath)

    def convertToSubTask(self):
        self.element_click("convert_to_sub_task_xpath", self.locators.convert_to_sub_task_xpath)

    def selectParentTask(self):
        self.element_click("select_parent_task_xpath", self.locators.select_parent_task_xpath)

    def subTaskView(self):
        self.element_click("sub_task_view_xpath", self.locators.sub_task_view_xpath)

    def subTaskRightClick(self):
        task_right_click = self.browser.find_element(By.XPATH, self.locators.sub_task_right_click_xpath)
        actions = ActionChains(self.browser)
        actions.context_click(task_right_click).perform()

    def convertToTask(self):
        self.element_click("convert_to_task_xpath", self.locators.convert_to_task_xpath)
