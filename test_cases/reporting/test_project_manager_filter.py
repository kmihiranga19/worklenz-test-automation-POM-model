from page_objects.Reporting.ProjectManagerFilter import ProjectManagerFilter
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
        self.ro = ProjectManagerFilter(self.driver)
        self.ro.reporting()
        self.ro.project_manger_filed_check()
        self.filtered_manger_name = self.ro.get_filtering_project_manager()
        self.manager_projects = self.ro.get_project_manager_projects(self.filtered_manger_name)
        self.ro.filtering_project_manager()
        self.filtered_projects = self.ro.get_projects_after_filtering()
        self.ro.check_filter_work_correctly(self.manager_projects, self.filtered_projects)

