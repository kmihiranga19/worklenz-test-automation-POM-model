from page_objects.Home.HomeTasks import HomeTasks
# from page_objects.Home.Home import ChangeProjectGroup
from page_objects.Login.login import Login
import time


class TestTasksByMeList:
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

    def test_tasks_by_me_list(self, setup):
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
        self.ht = HomeTasks(self.browser)
        time.sleep(3)
        self.ht.clickDropDown()
        time.sleep(3)
        self.ht.selectDropDown()
        time.sleep(3)
        self.ht.clickRefreshBtn()
        time.sleep(3)
        self.ht.enterTask(self.taskNameBy)
        time.sleep(3)
        self.ht.selectToday()
        time.sleep(3)
        self.ht.selectProject()
        time.sleep(3)
        self.ht.enterTask(self.taskName2By)
        time.sleep(3)
        self.ht.selectTomorrow()
        time.sleep(3)
        self.ht.selectProject()
        time.sleep(3)
        self.ht.enterTask(self.taskName3By)
        time.sleep(3)
        self.ht.selectNextWeek()
        time.sleep(3)
        self.ht.selectProject()
        time.sleep(3)
        self.ht.enterTask(self.taskName4By)
        time.sleep(3)
        self.ht.selectNextMonth()
        time.sleep(3)
        self.ht.selectProject()
        time.sleep(3)
        self.ht.enterTask(self.taskName5By)
        time.sleep(3)
        self.ht.selectNoDueDate()
        time.sleep(3)
        self.ht.selectProject()
        time.sleep(3)
        self.ht.clickTodayTab()
        time.sleep(3)
        self.ht.clickUpcomingTab()
        time.sleep(3)
        self.ht.clickOverdueTab()
        time.sleep(3)
        self.ht.clickNoDueDateTab()
        time.sleep(3)
        self.ht.clickAllTaskTab()
        time.sleep(3)
        self.ht.clickOpenTask()
        time.sleep(3)
        self.ht.clickAssigner()
        time.sleep(3)
        self.ht.unselectAssigner()
        time.sleep(5)
        self.ht.selectAssigner()
        time.sleep(3)
        self.ht.tempClick()
        time.sleep(3)
        self.ht.clickEndDate()
        time.sleep(3)
        self.ht.selectDate()
        time.sleep(3)
        self.ht.clickSubTask()
        time.sleep(3)
        self.ht.enterSubtask(self.subTask)
        time.sleep(3)
        self.ht.selectStatus()
        time.sleep(3)
        self.ht.selectDoing()
        time.sleep(5)
        self.ht.clickClose()
        time.sleep(3)
        self.ht.clickOutsideTaskDueDate()
        time.sleep(3)
        self.ht.selectOutsideTaskDueDate()
        time.sleep(3)
        self.ht.clickOutsideTaskStatus()
        time.sleep(3)
        self.ht.selectOutsideTaskStatus()
        time.sleep(5)