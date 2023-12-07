from page_objects.Reporting.Members import Members
from page_objects.Login.login import Login
import time
from test_data.test_data import ReportingMembersData
from utilities.readProperties import ReadConfig
from self import self


class TestReportingMembers:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_ReportingMembers(self, setup):
        self.browser = setup
        self.browser.get(self.baseURL)
        self.phase = ReportingMembersData()
        self.lg = Login(self.browser)
        self.lg.clickLogin()
        time.sleep(3)
        self.lg.setEmail(self.email)
        time.sleep(3)
        self.lg.setpassword(self.password)
        time.sleep(3)
        self.lg.submit()
        time.sleep(10)
        self.rm = Members(self.browser)
        time.sleep(3)
        self.rm.clickReportingTab()
        time.sleep(3)
        self.rm.clickMembersTab()
        time.sleep(3)
        self.rm.clickArchiveProject()
        time.sleep(3)
        self.rm.clickTimeRangeLastWeekBtn()
        time.sleep(3)
        self.rm.clickTimeRangeYesterday()
        time.sleep(3)
        self.rm.clickTimeRangeYesterdayBtn()
        time.sleep(3)
        self.rm.clickTimeRangeLastWeek()
        time.sleep(3)
        self.rm.clickTimeRangeLastWeekBtn()
        time.sleep(3)
        self.rm.clickTimeRangeLastMonth()
        time.sleep(3)
        self.rm.clickTimeRangeLastMonthBtn()
        time.sleep(3)
        self.rm.clickTimeRangeLastQuarter()
        time.sleep(3)
        self.rm.clickTimeRangeQuarterBtn()
        time.sleep(3)








