from page_objects.Login.login import Login
from page_objects.Workload.Workload import Workload
import time
from utilities.readProperties import ReadConfig
from self import self
from test_data.test_data import ProjectWorkloadData


class TestWorkload:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_workload(self, setup):
        self.browser = setup
        self.browser.get(self.baseURL)
        self.workloadData = ProjectWorkloadData()
        self.lg = Login(self.browser)
        time.sleep(3)
        self.lg.clickLogin()
        time.sleep(3)
        self.lg.setEmail(self.email)
        self.lg.setpassword(self.password)
        time.sleep(3)
        self.lg.submit()
        time.sleep(3)
        self.wl = Workload(self.browser)
        time.sleep(10)
        self.wl.clickProjectTab()
        time.sleep(10)
        self.wl.selectProject()
        time.sleep(3)
        self.wl.clickWorkloadTab()
        time.sleep(3)
        self.wl.clickCreateTaskBtn()
        time.sleep(3)
        self.wl.enterTaskName(self.workloadData.taskName)
        time.sleep(3)
        self.wl.clickAssigner()
        time.sleep(5)
        self.wl.selectAssigner()
        time.sleep(3)
        self.wl.clickTemporaryClick()
        time.sleep(3)
        self.wl.clickShowStartDate()
        time.sleep(3)
        self.wl.clickStartDate()
        time.sleep(3)
        self.wl.selectStartDate()
        time.sleep(3)
        self.wl.clickEndDate()
        time.sleep(3)
        self.wl.selectEndDate()
        time.sleep(3)
        self.wl.setHours(self.workloadData.EstimationDate)
        time.sleep(3)
        self.wl.clickDrawerClose()
        time.sleep(3)
        self.wl.clickExpandBtn()
        time.sleep(3)
        self.wl.OpenAssignedTask()
        time.sleep(3)
        self.wl.clickAddSubTask()
        time.sleep(3)
        self.wl.enterSubtask(self.workloadData.SubtaskName)
        time.sleep(3)
        self.wl.openSubTask()
        time.sleep(3)
        self.wl.clickAssigner()
        time.sleep(3)
        self.wl.selectSubTaskAssigner()
        time.sleep(3)
        self.wl.closeSubTask()
        time.sleep(5)
        self.wl.clickExpandBtn()
        time.sleep(10)



