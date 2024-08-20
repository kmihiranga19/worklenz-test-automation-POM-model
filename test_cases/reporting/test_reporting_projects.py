from page_objects.Reporting.ReportingProjects import ReportingProjects
from page_objects.Login.login import Login
from utilities.readProperties import ReadConfig


class TestReportingOverview:
    baseURL = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_reporting_projects(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = Login(self.driver)
        self.lg.enter_email(self.email)
        self.lg.enter_password(self.password)
        self.lg.submit()
        self.rp = ReportingProjects(self.driver)
        self.rp.go_to_project_tab()
        self.rp.get_own_teams()
        self.rp.get_own_team_projects_details()
