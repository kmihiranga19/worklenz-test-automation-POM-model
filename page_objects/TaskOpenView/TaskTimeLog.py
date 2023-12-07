from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import pyautogui
from page_objects.BasePage import Basepage
from page_objects.Locators import TaskTimeLogLocators


class TaskTimeLog(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = TaskTimeLogLocators()

    def clickProjectTab(self):
        self.element_click("project_tab_xpath", self.locators.project_tab_xpath)

    def selectProject(self):
        self.element_click("select_project_xpath", self.locators.select_project_xpath)

    def clickOpen(self):
        actions = ActionChains(self.browser)
        task = self.browser.find_element(By.XPATH, self.locators.div_taskName_xpath)
        actions.move_to_element(task).perform()
        time.sleep(2)
        self.browser.find_element(By.XPATH, self.locators.button_open_xpath).click()

    def clickTimeLogBtn(self):
        self.element_click("time_log_btn_xpath", self.locators.time_log_btn_xpath)

    def clickTimePlayBtn(self):
        self.element_click("time_play_btn_css", self.locators.time_play_btn_css)

    def clickTimeStopBtn(self):
        self.element_click("time_stop_btn_css", self.locators.time_stop_btn_css)

    def dateClear(self):
        actions = ActionChains(self.browser)
        task = self.browser.find_element(By.CSS_SELECTOR, self.locators.date_clear_css)
        actions.move_to_element(task).perform()
        time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR, self.locators.date_clear_css).click()

    def editTimeEditBtn(self):
        actions = ActionChains(self.browser)
        task = self.browser.find_element(By.XPATH, self.locators.edit_btn_xpath)
        actions.move_to_element(task).perform()
        time.sleep(2)
        self.browser.find_element(By.XPATH, self.locators.edit_btn_xpath).click()

    def setHours(self, hour):
        self.set_timelog(hour, "set_hours_xpath", self.locators.set_hours_xpath)

    def setMinutes(self, minutes):
        self.set_timelog(minutes, "set_minutes_xpath", self.locators.set_minutes_xpath)

    def setSeconds(self, seconds):
        self.set_timelog(seconds, "set_seconds_xpath", self.locators.set_seconds_xpath)

    def clickDatePicker(self):
        self.get_date_picker("date_picker_xpath", self.locators.date_picker_xpath)

    def selectDate(self):
        self.element_click("select_date_xpath", self.locators.select_date_xpath)

    def enterDescription(self, description):
        self.enter_input_name(description, "description_xpath", self.locators.description_xpath)

    def updateBtn(self):
        self.element_click("update_btn_xpath", self.locators.update_btn_xpath)

    def deleteTimeDeleteBtn(self):
        actions = ActionChains(self.browser)
        task = self.browser.find_element(By.XPATH, self.locators.delete_btn_xpath)
        actions.move_to_element(task).perform()
        time.sleep(2)
        self.browser.find_element(By.XPATH, self.locators.delete_btn_xpath).click()

    def clickOkBtn(self):
        self.element_click("delete_ok_btn_xpath", self.locators.delete_ok_btn_xpath)

    def clickAddTimeLog(self):
        self.element_click("add_time_log_btn_xpath", self.locators.add_time_log_btn_xpath)

    def clickExportToExcelBtn(self):
        self.element_click("export_to_excel_xpath", self.locators.export_to_excel_xpath)
