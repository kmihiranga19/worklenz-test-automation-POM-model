from page_objects.Login.login import Login
from page_objects.AdminCenter.AdminCenterOverview import AdminCenterOverview
from page_objects.AdminCenter.AdminCenterTeams import AdminCenterTeams
import time
from test_data.test_data import AdminCenterData
from utilities.readProperties import ReadConfig
from self import self


class TestAdminCenterTeams:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_team(self, setup):
        self.browser = setup
        self.browser.get(self.baseURL)
        self.adminCenter = AdminCenterData()
        self.lg = Login(self.browser)
        self.lg.clickLogin()
        time.sleep(3)
        self.lg.setEmail(self.email)
        self.lg.setpassword(self.password)
        time.sleep(3)
        self.lg.submit()
        time.sleep(10)
        self.ao = AdminCenterOverview(self.browser)
        time.sleep(3)
        self.ao.clickProfileIcon()
        time.sleep(3)
        self.ao.clickAdminBtn()
        time.sleep(3)
        self.tm = AdminCenterTeams(self.browser)
        time.sleep(3)
        self.tm.clickTeamBtn()
        time.sleep(3)
        self.tm.clickRefreshBtn()
        time.sleep(3)
        self.tm.clickAddTeamBtn()
        time.sleep(3)
        self.tm.enterTeamName(self.adminCenter.teamName)
        time.sleep(3)
        self.tm.createBtn()
        time.sleep(5)
        self.tm.searchByName(self.adminCenter.searchTName)
        time.sleep(3)
        self.tm.clickPageSelector()
        time.sleep(3)
        self.tm.click5Page()
        time.sleep(5)
