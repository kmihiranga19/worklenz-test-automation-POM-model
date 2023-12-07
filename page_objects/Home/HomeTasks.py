from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from page_objects.BasePage import Basepage
from page_objects.Locators import HomeTasksLocators


class HomeTasks(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = HomeTasksLocators()

    def clickRefreshBtn(self):
        self.element_click("refresh_btn_xpath", self.locators.refresh_btn_xpath)

    def enterTask(self, taskName):
        self.home_enter_task(taskName, "add_task_xpath", self.locators.add_task_xpath)

    def selectToday(self):
        self.element_click("today_xpath", self.locators.today_xpath)

    def selectTomorrow(self):
        self.element_click("tomorrow_xpath", self.locators.tomorrow_xpath)

    def selectNextWeek(self):
        self.element_click("next_week_xpath", self.locators.next_week_xpath)

    def selectNextMonth(self):
        self.element_click("next_month_xpath", self.locators.next_month_xpath)

    def selectNoDueDate(self):
        self.element_click("no_due_date_xpath", self.locators.no_due_date_xpath)

    def clickTodayTab(self):
        self.element_click("todayTab_xpath", self.locators.todayTab_xpath)

    def clickUpcomingTab(self):
        self.element_click("upcomingTab_xpath", self.locators.upcomingTab_xpath)

    def clickOverdueTab(self):
        self.element_click("overDueTab_xpath", self.locators.overDueTab_xpath)

    def clickNoDueDateTab(self):
        self.element_click("no_due_dateTab_xpath", self.locators.no_due_dateTab_xpath)

    def clickAllTaskTab(self):
        self.element_click("allTaskTab_xpath", self.locators.allTaskTab_xpath)

    def selectProject(self):
        self.element_click("project_select_xpath", self.locators.project_select_xpath)

    def clickOpenTask(self):
        actions = ActionChains(self.browser)
        task = self.browser.find_element(By.XPATH, self.locators.task_xpath)
        actions.move_to_element(task).perform()
        time.sleep(2)
        self.browser.find_element(By.XPATH, self.locators.task_open_xpath).click()

    def clickAssigner(self):
        self.element_click("assigner_xpath", self.locators.assigner_xpath)

    def unselectAssigner(self):
        self.element_click("unSelectAssigner_xpath", self.locators.unSelectAssigner_xpath)

    def selectAssigner(self):
        self.element_click("selectAssigner_xpath", self.locators.selectAssigner_xpath)

    def tempClick(self):
        self.element_click("temp_click_xpath", self.locators.temp_click_xpath)

    def clickEndDate(self):
        self.element_click("end_date_xpath", self.locators.end_date_xpath)

    def selectDate(self):
        self.element_click("select_date_xpath", self.locators.select_date_xpath)

    def clickSubTask(self):
        self.element_click("click_subTask_xpath", self.locators.click_subTask_xpath)

    def enterSubtask(self, subtask):
        self.enter_subTask(subtask,"enter_subTask_xpath", self.locators.enter_subTask_xpath)

    def selectStatus(self):
        self.element_click("status_xpath", self.locators.status_xpath)

    def selectDoing(self):
        self.element_click("doing_xpath", self.locators.doing_xpath)

    def clickClose(self):
        self.element_click("close_xpath", self.locators.close_xpath)

    def clickOutsideTaskDueDate(self):
        self.element_click("dueDate_click_task_outside_xpath", self.locators.dueDate_click_task_outside_xpath)

    def selectOutsideTaskDueDate(self):
        self.element_click("dueDate_select_task_outside_xpath", self.locators.dueDate_select_task_outside_xpath)

    def clickOutsideTaskStatus(self):
        self.element_click("task_outside_click_status", self.locators.task_outside_click_status)

    def selectOutsideTaskStatus(self):
        self.element_click("task_outside_change_status", self.locators.task_outside_change_status)

    def clickDropDown(self):
        self.element_click("click_dropDown_xpath", self.locators.click_dropDown_xpath)

    def selectDropDown(self):
        self.element_click("select_dropDown_xpath", self.locators.select_dropDown_xpath)

    def clickCalenderTab(self):
        self.element_click("calendar_tab_xpath", self.locators.calendar_tab_xpath)

    def clickYear(self):
        self.element_click("calender_year_xpath", self.locators.calender_year_xpath)

    def scroll_down(self):
        scroll_down = self.browser.find_element(By.XPATH, self.locators.scroll_xpath)
        self.browser.execute_script("arguments[0].scrollBy(0, 200);", scroll_down)

    def selectYear(self):
        self.element_click("calender_year_select_xpath", self.locators.calender_year_select_xpath)

    def clickMonth(self):
        self.element_click("calender_month_xpath", self.locators.calender_month_xpath)

    def selectMonth(self):
        self.element_click("calender_month_select_xpath", self.locators.calender_month_select_xpath)

    def selectDay(self):
        self.element_click("calender_date_select_xpath", self.locators.calender_date_select_xpath)

    def clickYearTab(self):
        self.element_click("calender_year_tab_xpath", self.locators.calender_year_tab_xpath)

    def selectNMonth(self):
        self.element_click("calender_month_change_xpath", self.locators.calender_month_change_xpath)
