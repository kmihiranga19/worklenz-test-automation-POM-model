from page_objects.BasePage import Basepage
from page_objects.Locators import ProjectInsightsLocators


class ProjectInsights(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = ProjectInsightsLocators()

    def clickProjectTab(self):
        self.element_click("project_tab_xpath", self.locators.project_tab_xpath)

    def selectProject(self):
        self.element_click("select_project_xpath", self.locators.select_project_xpath)

    def clickInsightTab(self):
        self.element_click("insight_tab_xpath", self.locators.insight_tab_xpath)

    def clickOverview(self):
        self.element_click("overview_xpath", self.locators.overview_xpath)

    def seeLastUpdatedTasks(self):
        self.element_click("last_updated_tasks_xpath", self.locators.last_updated_tasks_xpath)

    def clickMembers(self):
        self.element_click("members_selector_css", self.locators.members_selector_css)

    # def seeTaskByMembers(self):
    #     self.browser.find_element(By.CSS_SELECTOR, self.task_by_member_xpath).click()

    def clickTasks(self):
        self.element_click("tasks_xpath", self.locators.tasks_xpath)

    def seeOverDueTasks(self):
        self.element_click("overdue_tasks_xpath", self.locators.overdue_tasks_xpath)

    def seeOverLoggedTasks(self):
        self.element_click("over_logged_tasks_xpath", self.locators.over_logged_tasks_xpath)

    def seeCompletedEarlyTasks(self):
        self.element_click("task_completed_early_tasks_xpath", self.locators.task_completed_early_tasks_xpath)

    def seeCompletedLateTasks(self):
        self.element_click("task_completed_late_tasks_xpath", self.locators.task_completed_late_tasks_xpath)
