from page_objects.ProjectDetails.ProjectMembers import ProjectMembers
from page_objects.Login.login import Login
import time
from utilities.readProperties import ReadConfig
from self import self


class TestProjectMembers:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_project_members(self, setup):
        self.browser = setup
        self.browser.get(self.baseURL)
        self.lg = Login(self.browser)
        self.lg.clickLogin()
        time.sleep(3)
        self.lg.setEmail(self.email)
        self.lg.setpassword(self.password)
        time.sleep(3)
        self.lg.submit()
        time.sleep(3)
        self.pm = ProjectMembers(self.browser)
        time.sleep(3)
        self.pm.clickProjectTab()
        time.sleep(3)
        self.pm.selectProject()
        time.sleep(3)
        self.pm.clickMembers()
        time.sleep(3)
        self.pm.clickRefreshBtn()
        time.sleep(3)
        self.pm.clickRemoveBtn()
        time.sleep(3)
        self.pm.clickOkBtn()
        time.sleep(3)
        self.pm.clickPageSelector()
        time.sleep(3)
        self.pm.select5Page()
        time.sleep(5)
