from page_objects.ProjectDetails.ProjectWorkload import ProjectWorkload
from page_objects.Login.login import Login
import time
from test_data.test_data import ProjectWorkloadData
from utilities.readProperties import ReadConfig
from self import self


class TestProjectWorkload:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_project_workload(self, setup):
        self.browser = setup
        self.browser.get(self.baseURL)
        self.workloadData = ProjectWorkloadData()
        self.lg = Login(self.browser)
        self.lg.clickLogin()
        time.sleep(3)
        self.lg.setEmail(self.email)
        self.lg.setpassword(self.password)
        time.sleep(3)
        self.lg.submit()
        time.sleep(3)
        self.pw = ProjectWorkload(self.browser)
        time.sleep(10)
        self.pw.clickProjectTab()
        time.sleep(5)
        self.pw.selectProject()
        time.sleep(3)
        self.pw.clickCreateBtn()
        time.sleep(3)
        self.pw.enterTaskName(self.workloadData.taskName)
        time.sleep(3)
        self.pw.clickAssigner()
        time.sleep(3)
        self.pw.selectAssignMember()
        time.sleep(3)
        self.pw.clickTemp()
        time.sleep(3)
        self.pw.drawerClose()
        time.sleep(3)
        self.pw.clickWorkload()
        time.sleep(3)
        self.pw.memberOpen()
        time.sleep(3)
        self.pw.openTask()
        time.sleep(5)
