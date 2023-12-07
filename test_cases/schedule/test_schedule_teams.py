from page_objects.Login.login import Login
from page_objects.Schedule.ScheduleTeams import ScheduleTeams
import time
from utilities.readProperties import ReadConfig
from self import self


class TestScheduleTeams:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_schedule_teams(self, setup):
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
        self.st = ScheduleTeams(self.browser)
        time.sleep(3)
        self.st.clickScheduleTab()
        time.sleep(3)
        self.st.clickTeamsBtn()
        time.sleep(3)
        self.st.clickTeamsDropdown()
        time.sleep(3)
        self.st.clickTeamsDropdownClose()
        time.sleep(3)
        self.st.clickWeekSelector()
        time.sleep(3)
        self.st.clickPickDate()
        time.sleep(3)
        self.st.clickTimePeriod()
        time.sleep(3)
        self.st.clickTaskOpen()
        time.sleep(3)
        self.st.clickTaskClose()
        time.sleep(3)
        self.st.clickScheduleClose()
        time.sleep(5)
