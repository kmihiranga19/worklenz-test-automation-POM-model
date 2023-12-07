from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects.BasePage import Basepage
from page_objects.Locators import CreateProjectLocators


class CreateProject(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = CreateProjectLocators()

    def clickNewProjectTab(self):
        self.element_click("new_project_button_xpath",self.locators.new_project_button_xpath)

    def clickNameInput(self, projectName):
        self.enter_input_name(projectName,"name_input_xpath", self.locators.name_input_xpath)

    def clickProjectColor(self):
        self.element_click("project_color_xpath", self.locators.project_color_xpath)

    def selectProjectColor(self):
        self.element_click("select_project_color_xpath", self.locators.select_project_color_xpath)

    def clickStatusDropDown(self):
        self.element_click("status_dropdown_xpath", self.locators.status_dropDown_xpath)

    def selectStatus(self):
        self.element_click("in_progressOption_xpath", self.locators.in_progressOption_xpath)

    def enterNotes(self, notes):
        self.enter_input_name(notes,"notes_input_xpath", self.locators.notes_input_xpath)

    def enterClientInput(self, clientName):
        self.enter_client_input(clientName, "client_input_xpath", self.locators.client_input_xpath)

    def clickClientOption(self):
        self.element_click("client_option_xpath", self.locators.client_option_xpath)

    def clickStartDate(self):
        self.element_click("start_date_xpath", self.locators.start_date_xpath)

    def selectDate(self):
        self.element_click("select_date_xpath", self.locators.select_date_xpath)

    def clickEndDate(self):
        self.element_click("end_date_xpath", self.locators.end_date_xpath)

    def clickSubmitBtn(self):
        self.element_click("submit_button_xpath", self.locators.submit_button_xpath)

    def clickProjectTab(self):
        self.element_click("project_tab_xpath", self.locators.project_tab_xpath)

    def clickCreateProject(self):
        self.element_click("create_project_xpath", self.locators.create_project_xpath)

