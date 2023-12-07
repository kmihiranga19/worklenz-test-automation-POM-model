from page_objects.Login.login import Login
from page_objects.ProfileSettings.SettingsProfile import SettingsProfile
import time
from test_data.test_data import ProjectSettingsData
from utilities.readProperties import ReadConfig
from self import self


class TestSettingsProfile:
    baseURL = "https://uat.worklenz.com"
    email = "foveya5340@akoption.com"
    password = "ceyDigital#000"

    def test_settings_profile(self, setup):
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
        self.sp.selectImage()
        time.sleep(3)
        self.sp.enterName(self.projectSettingsData.name)
        time.sleep(3)
        self.sp.saveBtn()
        time.sleep(5)
