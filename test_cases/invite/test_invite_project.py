from page_objects.Login.login import Login
from page_objects.Invite.InviteProject import InviteProject
import time
from test_data.test_data import InviteData
from utilities.readProperties import ReadConfig
from self import self


class TestInviteProject:
    baseURL = ReadConfig.get_application_url(self)
    username = ReadConfig.get_userName()
    email = ReadConfig.get_inviteEmail()
    password = ReadConfig.get_password()

    def test_project_Invite(self, setup):
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
        self.ip = InviteProject(self.browser)
        time.sleep(3)
        self.ip.clickProjectTab()
        time.sleep(5)
        self.ip.clickCreateProjectBtn()
        time.sleep(3)
        self.ip.enterProjectName(self.InviteData.projectName)
        time.sleep(3)
        self.ip.clickProjectSubmitBtn()
        time.sleep(3)
        self.ip.clickInviteBtn()
        time.sleep(5)
        self.ip.enterInviteEmail(self.InviteData.inviteEmail)
        time.sleep(3)
        self.ip.deleteProjectMembers()
        time.sleep(3)
        self.ip.clickOkBtn()
        time.sleep(3)
