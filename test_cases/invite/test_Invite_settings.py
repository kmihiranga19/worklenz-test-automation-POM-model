from page_objects.Login.login import Login
from page_objects.Invite.InviteSettings import InviteSettings
import time
from test_data.test_data import InviteData
from utilities.readProperties import ReadConfig
from self import self


class TestInviteSettings:
    baseURL = ReadConfig.get_application_url(self)
    username = ReadConfig.get_userName()
    email = ReadConfig.get_inviteEmail()
    password = ReadConfig.get_password()

    def test_project_settings(self, setup):
        self.browser = setup
        self.browser.get(self.baseURL)
        self.InviteData = InviteData()
        self.lg = Login(self.browser)
        time.sleep(3)
        self.lg.clickLogin()
        time.sleep(3)
        self.lg.setEmail(self.InviteData.loginEmail)
        self.lg.setpassword(self.password)
        time.sleep(3)
        self.lg.submit()
        time.sleep(10)
        self.ns = InviteSettings(self.browser)
        time.sleep(3)
        self.ns.clickProfile()
        time.sleep(3)
        self.ns.clickSettings()
        time.sleep(3)
        self.ns.clickTeamMembersTab()
        time.sleep(3)
        self.ns.clickAddBtn()
        time.sleep(5)
        self.ns.clickInviteMember()
        time.sleep(3)
        self.ns.enterInviteMember(self.InviteData.inviteEmail)
        time.sleep(3)
        self.ns.clickJobTitle(self.InviteData.job_title)
        time.sleep(3)
        self.ns.clickAccess()
        time.sleep(3)
        self.ns.selectAccess()
        time.sleep(3)
        self.ns.clickSubmitBtn()
        time.sleep(5)
