from page_objects.Login.login import Login
from page_objects.ProfileSettings.SettingsProfile import SettingsProfile
from page_objects.ProfileSettings.SettingsNotifications import SettingsNotifications
import time
from test_data.test_data import ProjectSettingsData
from utilities.readProperties import ReadConfig
from self import self


class TestSettingsNotifications:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_settings_notifications(self, setup):
        self.browser = setup
        self.browser.get(self.baseURL)
        self.projectSettingsData = ProjectSettingsData()
        self.lg = Login(self.browser)
        self.lg.clickLogin()
        time.sleep(3)
        self.lg.setEmail(self.email)
        self.lg.setpassword(self.password)
        time.sleep(3)
        self.lg.submit()
        time.sleep(3)
        self.sp = SettingsProfile(self.browser)
        time.sleep(3)
        self.sp.clickProfileIcon()
        time.sleep(3)
        self.sp.clickSettings()
        time.sleep(3)
        self.sn = SettingsNotifications(self.browser)
        self.sn.clickNotificationsTab()
        time.sleep(3)
        self.sn.clickEmailNotifications()
        time.sleep(2)
        self.sn.clickEmailNotifications()
        time.sleep(2)
        self.sn.clickDailyDigest()
        time.sleep(2)
        self.sn.clickDailyDigest()
        time.sleep(2)
        self.sn.clickPushNotifications()
        time.sleep(2)
        self.sn.clickPushNotifications()
        time.sleep(2)
        self.sn.clickUnreadItem()
        time.sleep(2)
        self.sn.clickUnreadItem()
        time.sleep(5)
