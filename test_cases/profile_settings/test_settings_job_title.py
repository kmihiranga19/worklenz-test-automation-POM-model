from page_objects.Login.login import Login
from page_objects.ProfileSettings.SettingsProfile import SettingsProfile
from page_objects.ProfileSettings.SettingsJobTitle import SettingsJobTitle
import time
from test_data.test_data import ProjectSettingsData
from utilities.readProperties import ReadConfig
from self import self


class TestSettingsJobTitle:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_settings_job_title(self, setup):
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
        self.sj = SettingsJobTitle(self.browser)
        time.sleep(3)
        self.sj.clickJobTitleTab()
        time.sleep(3)
        self.sj.clickClientJobTitle()
        time.sleep(3)
        self.sj.enterName(self.projectSettingsData.JobName)
        time.sleep(3)
        self.sj.clickCreateBtn()
        time.sleep(3)
        self.sj.searchByName(self.projectSettingsData.JobSearchByName)
        time.sleep(3)
        self.sj.clickJobEditBtn()
        time.sleep(3)
        self.sj.jobNameUpdate()
        time.sleep(3)
        self.sj.clickUpdateBtn()
        time.sleep(3)
        self.sj.clickDeleteBtn()
        time.sleep(3)
        self.sj.clickYesBtn()
        time.sleep(3)
        self.sj.clickPinClient()
        time.sleep(3)
        self.sj.clickUnPinClient()
        time.sleep(3)
        self.sj.clickPageSelector()
        time.sleep(3)
        self.sj.clickPageSelect()
        time.sleep(5)
