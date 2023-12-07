from page_objects.Login.login import Login
from page_objects.ProfileSettings.SettingsProfile import SettingsProfile
from page_objects.ProfileSettings.SettingsTeamMember import SettingsTeamMember
import time
from test_data.test_data import ProjectSettingsData
from utilities.readProperties import ReadConfig
from self import self


class TestSettingsTeamMember:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_settings_teamMember(self, setup):
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
        self.sm = SettingsTeamMember(self.browser)
        time.sleep(3)
        self.sm.clickTeamMemberTab()
        time.sleep(3)
        self.sm.clickRefreshBtn()
        time.sleep(3)
        self.sm.searchMember(self.projectSettingsData.searchMemberName)
        time.sleep(3)
        self.sm.clickAddMemberBtn()
        time.sleep(3)
        self.sm.enterEmail(self.projectSettingsData.inviteEmail)
        time.sleep(3)
        self.sm.clickMemberEdit()
        time.sleep(3)
        self.sm.clickJobTitle()
        time.sleep(3)
        self.sm.selectTitle()
        time.sleep(3)
        self.sm.clickAccess()
        time.sleep(3)
        self.sm.selectAccess()
        time.sleep(3)
        self.sm.clickUpdateBtn()
        time.sleep(3)
        self.sm.clickDeleteBtn()
        time.sleep(3)
        self.sm.clickDeleteYesBtn()
        time.sleep(3)
        self.sm.clickPageSelector()
        time.sleep(3)
        self.sm.clickPageSelect()
        time.sleep(5)
