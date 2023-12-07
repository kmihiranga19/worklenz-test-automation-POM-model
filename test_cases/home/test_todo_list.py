from page_objects.Home.HomeTodoList import HomeTodoList
# from page_objects.Home.Home import ChangeProjectGroup
from page_objects.Login.login import Login
import time


class TestTodoList:
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

    def test_todo_list(self, setup):
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
        self.htd = HomeTodoList(self.browser)
        time.sleep(3)
        self.htd.enterToDoTask(self.todoTask)
        time.sleep(5)
        self.htd.enterToDoTask(self.todoTask2)
        time.sleep(3)
        self.htd.clickRefreshBtn()
        time.sleep(3)
        self.htd.clickDoneBtn()
        time.sleep(5)
        self.htd.clickDoneBtn()
        time.sleep(8)