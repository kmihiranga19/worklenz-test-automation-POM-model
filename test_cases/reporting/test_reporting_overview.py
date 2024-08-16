from page_objects.Reporting.ReportingOverview import ReportingOverview
from page_objects.Login.login import Login
from utilities.readProperties import ReadConfig


class TestReportingOverview:
    baseURL = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_reporting_overview(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = Login(self.driver)
        self.lg.enter_email(self.email)
        self.lg.enter_password(self.password)
        self.lg.submit()
        self.ro = ReportingOverview(self.driver)
        self.ro.go_to_reporting()
        self.ro.open_team_selection()
        self.ro.get_owner_you_team()
        self.ro.get_own_you_teams_project_count()
        self.ro.go_to_reporting()
        self.reporting_team_count, self.reporting_project_count, self.members_count_reporting = self.ro.get_reporting_overview_first_card_details()
        self.ro.check_overview_first_card(self.reporting_team_count, self.reporting_project_count, self.members_count_reporting)
        self.ro.get_active_overdue_projects_count()
        self.active_projects_count, self.overdue_projects_count = self.ro.get_reporting_active_overdue_projects_count()
        self.ro.check_active_overdue_projects_count(self.active_projects_count, self.overdue_projects_count)
