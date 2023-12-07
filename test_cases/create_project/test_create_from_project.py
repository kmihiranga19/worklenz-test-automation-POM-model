from page_objects.CreateProject.CreateProject import CreateProject
from page_objects.Login.login import Login
import time
from test_data.test_data import CreateProjectData
from utilities.readProperties import ReadConfig
from self import self


class TestProjectInsights:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_project_project(self, setup):
        self.browser = setup
        self.browser.get(self.baseURL)
        self.createProject = CreateProjectData()
        self.lg = Login(self.browser)
        self.lg.clickLogin()
        time.sleep(3)
        self.lg.setEmail(self.email)
        self.lg.setpassword(self.password)
        time.sleep(3)
        self.lg.submit()
        time.sleep(10)
        self.cm = CreateProject(self.browser)
        time.sleep(3)
        self.cm.clickProjectTab()
        time.sleep(8)
        self.cm.clickCreateProject()
        time.sleep(3)
        self.cm.clickNameInput(self.createProject.projectName2)
        time.sleep(3)
        self.cm.clickProjectColor()
        time.sleep(3)
        self.cm.selectProjectColor()
        time.sleep(3)
        self.cm.clickStatusDropDown()
        time.sleep(3)
        self.cm.selectStatus()
        time.sleep(3)
        self.cm.enterNotes(self.createProject.notes2)
        time.sleep(3)
        self.cm.enterClientInput(self.createProject.clientName)
        time.sleep(3)
        self.cm.clickStartDate()
        time.sleep(3)
        self.cm.selectDate()
        time.sleep(3)
        self.cm.clickEndDate()
        time.sleep(3)
        self.cm.selectDate()
        time.sleep(3)
        self.cm.clickSubmitBtn()
        time.sleep(5)
        self.cm.clickProjectTab()
        time.sleep(10)
