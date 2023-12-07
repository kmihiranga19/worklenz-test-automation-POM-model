from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects.BasePage import Basepage
from selenium.webdriver import ActionChains
import time
from page_objects.Locators import ImportTaskLocators


class ImportTask(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = ImportTaskLocators()

    def clickProjectTab(self):
        self.element_click(" project_tab_xpath", self.locators.project_tab_xpath)

    def selectProject(self):
        self.element_click("select_project_xpath", self.locators.select_project_xpath)

    def clickImportDownIcon(self):
        self.element_click("import_down_icon_xpath", self.locators.import_down_icon_xpath)

    def clickImport(self):
        self.element_click("import_task_xpath", self.locators.import_task_xpath)

    def clickTempInput(self):
        self.element_click("temp_input_xpath", self.locators.temp_input_xpath)

    def selectTemp(self):
        self.element_click("select_temp_xpath", self.locators.select_temp_xpath)

    def removeOneTask(self):
        self.element_click("remove_task_xpath", self.locators.remove_task_xpath)

    def clickImportBtn(self):
        self.element_click("import_btn_xpath", self.locators.import_btn_xpath)

    def clickCreateBtn(self):
        self.element_click("create_project_xpath", self.locators.create_project_xpath)

    def enterProjectName(self, projectName):
        self.enter_input_name(projectName, "project_name_xpath", self.locators.project_name_xpath)

    def clickProjectSubmitBtn(self):
        self.element_click("create_btn_xpath", self.locators.create_btn_xpath)
