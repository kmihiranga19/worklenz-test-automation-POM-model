from page_objects.Home.Bugs import ChangeProjectGroup
from page_objects.Login.login import Login
import time


class TestProject:
    baseURL = "https://uat.worklenz.com"
    email = "foveya5340@akoption.com"
    password = "ceyDigital#000"
    taskNameTo = "Home task to me"
    taskName2To = "Home task 2 to me"
    taskName3to = "Home task 3 to me "
    taskName4To = "Home task 4 to me"
    taskName5To = "Home task 5 to me"
    taskNameBy = "Home task by me"
    taskName2By = "Home task 2 by me"
    taskName3By = "Home task 3 by me "
    taskName4By = "Home task 4 by me"
    taskName5By = "Home task 5 by me"
    calender_select_task = "Selecting date task"
    subTask = "This is sub task"
    todoTask = "To do task 1"
    todoTask2 = "To do task 2"
    testingTask = "Testing Task"
    testingSubTask = "Testing Sub Task"

    def test_change_group(self, setup):
        self.browser = setup
        self.browser.get(self.baseURL)
        self.lg = Login(self.browser)
        self.lg.clickLogin()
        time.sleep(3)
        self.lg.setEmail(self.email)
        self.lg.setpassword(self.password)
        time.sleep(3)
        self.lg.submit()
        time.sleep(10)
        self.hpg = ChangeProjectGroup(self.browser)
        time.sleep(3)
        self.hpg.select_project()
        time.sleep(3)
        self.hpg.clickProjectGroup()
        time.sleep(3)
        self.hpg.selectPhase()
        time.sleep(3)
        self.hpg.clickHome()
        time.sleep(3)
        self.hpg.enterTask(self.testingTask)
        time.sleep(3)
        self.hpg.selectDueDate()
        time.sleep(3)
        self.hpg.selectProject()
        time.sleep(5)
        self.hpg.clickOpenTask()
        time.sleep(3)
        self.hpg.clickSubTask()
        time.sleep(3)
        self.hpg.enterSubtask(self.testingSubTask)
        time.sleep(8)

