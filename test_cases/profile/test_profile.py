from page_objects.Profile.Profile import Profile
from page_objects.Login.login import Login
import time
from utilities.readProperties import ReadConfig
from self import self


class TestProfile:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_profile(self, setup):
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
        time.sleep(10)
        self.pi = Profile(self.browser)
        self.pi.profile_icon()
        time.sleep(3)
        self.pi.admin_center()
        time.sleep(3)
        self.pi.profile_icon2()
        time.sleep(3)
        self.pi.settings()
        time.sleep(5)
        self.pi.profile_icon2()
        time.sleep(5)
        self.pi.log_out()
        time.sleep(5)
        self.pi.close()

