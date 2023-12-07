from page_objects.Login.login import Login
from page_objects.AdminCenter.AdminCenterOverview import AdminCenterOverview
from page_objects.AdminCenter.AdminCenterUsers import AdminCenterUsers
import time
from test_data.test_data import AdminCenterData
from utilities.readProperties import ReadConfig
from self import self


class TestAdminCenterUsers:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_users(self, setup):
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
        self.us = AdminCenterUsers(self.browser)
        time.sleep(3)
        self.us.clickUsersBtn()
        time.sleep(3)
        self.us.clickRefreshBtn()
        time.sleep(3)
        self.us.searchByName(self.adminCenter.searchName)
        time.sleep(3)
        self.us.clickPageSelector()
        time.sleep(3)
        self.us.clickPage5()
        time.sleep(5)
