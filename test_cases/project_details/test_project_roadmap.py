from page_objects.ProjectDetails.ProjectRoadmap import ProjectRoadmap
from page_objects.Login.login import Login
import time
from utilities.readProperties import ReadConfig
from self import self


class TestProjectRoadmap:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_project_workload(self, setup):
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
        self.rm = ProjectRoadmap(self.browser)
        time.sleep(3)
        self.rm.clickProjectTab()
        time.sleep(3)
        self.rm.selectProject()
        time.sleep(3)
        self.rm.clickRoadMap()
        time.sleep(5)
