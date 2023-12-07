from page_objects.Login.login import Login
from page_objects.LogOut.LogOut import LogOut
import time
from utilities.readProperties import ReadConfig
from self import self


class TestlogOut:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_logout(self, setup):
        self.browser = setup
        self.browser.get(self.baseURL)
        self.lg = Login(self.browser)
        time.sleep(3)
        self.lg.clickLogin()
        time.sleep(3)
        self.lg.setEmail(self.email)
        self.lg.setpassword(self.password)
        time.sleep(3)
        self.lg.submit()
        time.sleep(3)
        self.lo = LogOut(self.browser)
        time.sleep(3)
        self.lo.clickProfileIcon()
        time.sleep(3)
        self.lo.clickLogOutBtn()
        time.sleep(3)
        self.lo.clickOkBtn()
        time.sleep(5)
