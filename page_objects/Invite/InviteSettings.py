from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects.BasePage import Basepage
from page_objects.Locators import InviteSettingsLocators


class InviteSettings(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = InviteSettingsLocators

    def clickProfile(self):
        self.element_click("profile_icon_xpath", self.locators.profile_icon_xpath)

    def clickSettings(self):
        self.element_click("settings_xpath", self.locators.settings_xpath)

    def clickTeamMembersTab(self):
        self.element_click("click_team_membersTab_xpath", self.locators.click_team_membersTab_xpath)

    def clickAddBtn(self):
        self.element_click("add_member_xpath", self.locators.add_member_xpath)

    def clickInviteMember(self):
        self.element_click("invite_member_xpath", self.locators.invite_member_xpath)

    def enterInviteMember(self, inviteEmail):
        self.enter_invite_email(inviteEmail, "enter_invite_member_xpath", self.locators.enter_invite_member_xpath)

    def clickJobTitle(self, jobTitle):
        self.enter_input_name(jobTitle, "job_title_xpath", self.locators.job_title_xpath)

    def clickAccess(self):
        self.element_click("access_xpath", self.locators.access_xpath)

    def selectAccess(self):
        self.element_click("select_access_xpath", self.locators.select_access_xpath)

    def clickSubmitBtn(self):
        self.element_click("submit_btn_xpath", self.locators.submit_btn_xpath)
