from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects.BasePage import Basepage
from page_objects.Locators import SignUpLocators, InviteOnboardingLocators


class SignUp(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = SignUpLocators()

    def clickLoginBtn(self):
        self.element_click("login_btn_xpath", self.locators.login_btn_xpath)

    def clickSignBtn(self):
        self.element_click("signUP_btn_xpath", self.locators.signUp_btn_xpath)

    def enterName(self, name):
        self.enter_input_name(name, "enter_name_xpath", self.locators.enter_name_xpath)

    def enterEmail(self, email):
        self.enter_input_name(email, "enter_email_xpath", self.locators.enter_email_xpath)

    def enterPassword(self, password):
        self.enter_input_name(password, "enter_password_xpath", self.locators.enter_password_xpath)

    def clickSubmitBtn(self):
        self.element_click("submit_xpath", self.locators.submit_xpath)


class InviteOnboarding(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = InviteOnboardingLocators()

    def enterOrganizationName(self, orgName):
        self.enter_input_name(orgName, "enter_organization_xpath", self.locators.enter_organization_xpath)

    def clickContinueBtn1(self):
        self.element_click("continue_btn1_xpath", self.locators.continue_btn1_xpath)

    def enterProjectName(self, project):
        self.enter_input_name(project, "enter_project_xpath", self.locators.enter_project_xpath)

    def clickContinueBtn2(self):
        self.element_click("continue_btn2_xpath", self.locators.continue_btn2_xpath)

    def enterTask(self, task):
        self.enter_input_name(task, "enter_task_xpath", self.locators.enter_task_xpath)

    def enterInviteEmail(self, inviteEmail):
        self.enter_input_name(inviteEmail, "enter_inviteEmail_tag", self.locators.enter_inviteEmail_tag)
