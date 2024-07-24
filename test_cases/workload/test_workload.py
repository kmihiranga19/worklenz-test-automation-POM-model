from page_objects.Login.login import Login
from page_objects.Workload.Workload import Workload
import time
from utilities.readProperties import ReadConfig
from self import self
from test_data.test_data import ProjectWorkloadData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


class TestWorkload:
    baseURL = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_workload_act(self, setup):
        self.browser = setup
        self.browser.get(self.baseURL)
        self.workloadData = ProjectWorkloadData()
        self.lg = Login(self.browser)
        self.lg.enter_email(self.email)
        self.lg.enter_password(self.password)
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

    def test_a(self, setup):
        self.email1 = "ss@d.com"
        self.psw = "ceyDigital#00"
        self.driver = setup
        self.driver.get("https://app.worklenz.com/auth/login")
        self.lg = Login(self.driver)
        self.lg.enter_email(self.email1)
        self.lg.enter_password(self.psw)
        self.lg.submit()
        self.wrl = Workload(self.driver)
        self.wrl.go_to_projects()
        if self.driver.current_url == "https://app.worklenz.com/worklenz/projects":
            self.teams = self.wrl.get_teams()
            self.wrl.workload_main(self.teams)

        else:
            print("Your are not navigate correct page")









