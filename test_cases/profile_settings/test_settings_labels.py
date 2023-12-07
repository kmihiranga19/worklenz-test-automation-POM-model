from page_objects.Login.login import Login
from page_objects.ProfileSettings.SettingsProfile import SettingsProfile
from page_objects.ProfileSettings.SettingsLabels import SettingsLabels
import time
from test_data.test_data import ProjectSettingsData
from utilities.readProperties import ReadConfig
from self import self


class TestSettingsLabels:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_settings_labels(self, setup):
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
        self.sl = SettingsLabels(self.browser)
        time.sleep(3)
        self.sl.clickLabelTab()
        time.sleep(3)
        self.sl.labelSearch(self.projectSettingsData.labelSearchName)
        time.sleep(3)
        self.sl.clickPinClient()
        time.sleep(3)
        self.sl.clickUnPinClient()
        time.sleep(5)
