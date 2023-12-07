from page_objects.Login.login import Login
from page_objects.Schedule.ScheduleProject import ScheduleProject
import time
from utilities.readProperties import ReadConfig
from self import self


class TestScheduleProject:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_schedule_project(self, setup):
        self.browser = setup
        self.browser.get(self.baseURL)
        self.lg = Login(self.browser)
        time.sleep(3)
        self.lg.clickLogin()
        time.sleep(3)
        self.lg.setEmail(self.email)
        self.lg.setpassword(self.password)
        time.sleep(3)
        self.lg.submit()
        time.sleep(10)
        self.sp = ScheduleProject(self.browser)
        time.sleep(3)
        self.sp.clickScheduleTab()
        time.sleep(3)
        self.sp.clickProjectDropdown()
        time.sleep(3)
        self.sp.clickWeekSelector()
        time.sleep(3)
        self.sp.clickTimePeriod()
        time.sleep(3)
        self.sp.clickTask()
        time.sleep(3)
        self.sp.clickCloseBtn()
        time.sleep(3)
        self.sp.clickCloseBtn2()
        time.sleep(5)
