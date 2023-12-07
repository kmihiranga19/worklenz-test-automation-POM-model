from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects.BasePage import Basepage
from page_objects.Locators import InviteProjectLocators


class InviteProject(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = InviteProjectLocators()

    def clickProjectTab(self):
        self.element_click("project_tab_xpath", self.locators.project_tab_xpath)

    def clickCreateProjectBtn(self):
        self.element_click("create_project_btn_xpath", self.locators.create_project_btn_xpath)

    def enterProjectName(self, projectName):
        self.enter_input_name(projectName, "project_name_input_xpath", self.locators.project_name_input_xpath)

    def clickProjectSubmitBtn(self):
        self.element_click("project_submit_btn_xpath", self.locators.project_submit_btn_xpath)

    def clickProject(self):
        self.element_click("select_project_xpath", self.locators.select_project_xpath)

    def clickInviteBtn(self):
        self.element_click("invite_btn_xpath", self.locators.invite_btn_xpath)

    def deleteProjectMembers(self):
        self.element_click("delete_project_members_xpath", self.locators.delete_project_members_xpath)

    def clickOkBtn(self):
        self.element_click("ok_btn_xpath", self.locators.ok_btn_xpath)

    def enterInviteEmail(self, inviteEmail):
        self.enter_invite_email(inviteEmail, "enter_invite_email_xpath", self.locators.enter_invite_email_xpath)
