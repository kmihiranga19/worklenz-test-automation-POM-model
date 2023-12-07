from page_objects.Login.login import Login
from page_objects.ProfileSettings.SettingsProfile import SettingsProfile
from page_objects.ProfileSettings.SettingsClients import SettingsClients
import time
from test_data.test_data import ProjectSettingsData
from utilities.readProperties import ReadConfig
from self import self


class TestSettingsClients:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_settings_clients(self, setup):
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
        self.sc = SettingsClients(self.browser)
        time.sleep(3)
        self.sc.clickCreateBtn()
        time.sleep(3)
        self.sc.enterName(self.projectSettingsData.clientName)
        time.sleep(3)
        self.sc.createButton()
        time.sleep(3)
        self.sc.searchByName(self.projectSettingsData.SearchClientName)
        time.sleep(3)
        self.sc.clientNameEditBtn()
        time.sleep(3)
        self.sc.clientNameUpdateBtn(self.projectSettingsData.clientUpdateName)
        time.sleep(3)
        self.sc.clickUpdateBtn()
        time.sleep(3)
        self.sc.clickDeleteBtn()
        time.sleep(3)
        self.sc.clickDeleteYesBtn()
        time.sleep(3)
        self.sc.clickPinClient()
        time.sleep(3)
        self.sc.clickUnPinClient()
        time.sleep(3)
        self.sc.clickPageSelector()
        time.sleep(3)
        self.sc.clickPageSelect()
        time.sleep(5)
