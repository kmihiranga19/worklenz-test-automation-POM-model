from page_objects.Invite.InviteOnboarding import SignUp
from page_objects.Invite.InviteOnboarding import InviteOnboarding
import time
from test_data.test_data import InviteData
from utilities.readProperties import ReadConfig
from self import self


class TestInviteOnboarding:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_userName()
    email = ReadConfig.get_inviteEmail()
    password = ReadConfig.get_password()

    def test_invite_onboarding(self, setup):
        self.browser = setup
        self.browser.get(self.baseURL)
        self.Invite = InviteData()
        self.su = SignUp(self.browser)
        time.sleep(3)
        self.su.clickSignBtn()
        time.sleep(3)
        self.su.enterName(self.username)
        self.su.enterEmail(self.email)
        self.su.enterPassword(self.password)
        time.sleep(3)
        self.su.clickSubmitBtn()
        time.sleep(3)
        self.it = InviteOnboarding(self.browser)
        time.sleep(5)
        self.it.enterOrganizationName(self.Invite.orgName)
        time.sleep(3)
        self.it.clickContinueBtn1()
        time.sleep(3)
        self.it.enterProjectName(self.Invite.project)
        time.sleep(3)
        self.it.clickContinueBtn1()
        time.sleep(3)
        self.it.enterTask(self.Invite.task)
        time.sleep(3)
        self.it.clickContinueBtn1()
        time.sleep(3)
        self.it.enterInviteEmail(self.Invite.inviteEmail)
        time.sleep(3)
        self.it.clickContinueBtn1()
        time.sleep(15)
