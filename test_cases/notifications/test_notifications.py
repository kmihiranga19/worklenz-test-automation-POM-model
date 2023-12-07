from page_objects.Login.login import Login
from page_objects.Notificatons.Notifications import Notifications
import time
from utilities.readProperties import ReadConfig
from self import self


class TestNotifications:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_notifications(self, setup):
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
        self.no = Notifications(self.browser)
        time.sleep(3)
        self.no.clickNotificationsIcon()
        time.sleep(3)
        self.no.clickMarkRead()
        time.sleep(3)
        self.no.clickReadBtn()
        time.sleep(3)
        self.no.clickUnreadBtn()
        time.sleep(3)
        self.no.clickMarkAllRead()
        time.sleep(3)
        self.no.clickReadBtn()
        time.sleep(3)
        # self.no.clickJoinBtn()
        # time.sleep(3)
        self.no.clickCloseBtn()
        time.sleep(3)
        self.browser.close()
