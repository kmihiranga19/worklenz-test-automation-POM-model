from page_objects.Invite.InviteOnboarding import InviteOnboarding
import time
from test_data.test_data import InviteData
from utilities.readProperties import ReadConfig
from selenium.webdriver.remote.webdriver import WebDriver


class TestInviteOnboarding:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_userName()
    email = ReadConfig.get_inviteEmail()
    password = ReadConfig.get_password()

    def test_invite_Onboarding(self, setup):
        self.driver = setup
        self.driver.get("https://uat.app.worklenz.com/auth/signup")
        self.lg = InviteOnboarding(self.driver)
        self.lg.signUp()
        self.organization_name = self.lg.give_organization_name()
        self.project_name = self.lg.create_first_project()
        self.lg.create_first_tasks()
        self.lg.invite_team_members()
        # self.lg.skip_invite_team_members()
        self.created_organization_name = self.lg.get_organization_name()
        self.created_project_name = self.lg.get_project_name()
        self.created_tasks_name = self.lg.get_project_tasks()
        self.lg.check_organization_name(self.organization_name, self.created_organization_name)
        self.lg.check_project_name(self.project_name, self.created_project_name)
        self.lg.check_project_tasks(self.created_tasks_name)



