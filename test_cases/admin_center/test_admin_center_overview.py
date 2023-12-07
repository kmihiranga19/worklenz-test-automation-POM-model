from page_objects.Login.login import Login
from page_objects.AdminCenter.AdminCenterOverview import AdminCenterOverview
import time
from test_data.test_data import AdminCenterData
from utilities.readProperties import ReadConfig
from self import self
from utilities.test_utils import sleep3, sleep5


class TestAdminCenterOverview:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_overview(self, setup):
        self.browser = setup
        self.browser.get(self.baseURL)
        self.adminCenter = AdminCenterData()
        self.lg = Login(self.browser)
        self.lg.clickLogin()
        sleep3()
        self.lg.setEmail(self.email)
        self.lg.setpassword(self.password)
        sleep3()
        self.lg.submit()
        time.sleep(10)
        self.ao = AdminCenterOverview(self.browser)
        time.sleep(3)
        self.ao.clickProfileIcon()
        time.sleep(3)
        self.ao.clickAdminBtn()
        time.sleep(3)
        self.ao.organizationName()
        time.sleep(3)
        self.ao.enterName(self.adminCenter.name)
        time.sleep(3)
        self.ao.organizationOwner()
        time.sleep(3)
        self.ao.organizationNo(self.adminCenter.number)
        time.sleep(5)
