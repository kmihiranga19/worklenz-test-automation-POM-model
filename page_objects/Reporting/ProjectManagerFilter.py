import time
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from faker import Faker
import re
import csv


class ProjectManagerFilter:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def reporting(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//strong[normalize-space()='Reporting']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//li[@class='ant-menu-item'][normalize-space()='Projects']"))).click()

    def project_manger_filed_check(self):
        head_wrapper = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ant-card-head-wrapper")))
        head_wrapper_wait = WebDriverWait(head_wrapper, 10)
        button = head_wrapper_wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))[4]
        button_wait = WebDriverWait(button, 10)
        button_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "span")))[1].click()
        show_filed_items_menu = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "ant-dropdown-menu-vertical")))
        show_filed_items_menu_wait = WebDriverWait(show_filed_items_menu, 10)
        manger_checkbox = \
            show_filed_items_menu_wait.until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "ant-dropdown-menu-item")))[
                -1]
        manger_checkbox_class_name = manger_checkbox.get_attribute("class")

        if "ant-checkbox-wrapper-checked" not in manger_checkbox_class_name:
            manger_checkbox.click()

        else:
            button.click()

    def get_filtering_project_manager(self):
        not_need_span = '<input type="checkbox" class="ant-checkbox-input ng-untouched ng-pristine ng-valid"><span class="ant-checkbox-inner"></span>'
        head_wrapper = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ant-card-head-wrapper")))
        head_wrapper_wait = WebDriverWait(head_wrapper, 10)
        button = head_wrapper_wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))[3]
        button_wait = WebDriverWait(button, 10)
        button_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "span")))[1].click()
        time.sleep(4)
        drop_down_menu = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ant-dropdown-menu-vertical")))
        drop_down_menu_wait = WebDriverWait(drop_down_menu, 20)
        project_manger = drop_down_menu_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "li")))[1]
        project_manger_wait = WebDriverWait(project_manger, 20)
        span_tags = project_manger_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "span")))
        for span_tag in span_tags:
            if span_tag.get_attribute('innerHTML') != "":
                if span_tag.get_attribute('innerHTML') == not_need_span:
                    continue
                project_manager_name = span_tag.get_attribute('innerHTML')
                return project_manager_name.strip()

    def get_project_manager_projects(self, filtered_manager_name):
        projects_details = []

        table = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))
        time.sleep(2)
        rows = table.find_elements(By.TAG_NAME, "tr")
        for index, row in enumerate(rows):
            project_details = {
                "project_name": "",
                "project_manager_name": ""
            }
            if index == 0:
                continue
            project_name = row.find_elements(By.TAG_NAME, "td")[0].text
            manager_cell = row.find_elements(By.TAG_NAME, "td")[-1]
            try:
                manager_cell.find_element(By.TAG_NAME, "worklenz-na")

            except NoSuchElementException:
                manager = manager_cell.find_elements(By.TAG_NAME, "span")[1].text
                manager_name = manager.strip()
                if manager_name == filtered_manager_name:
                    project_details["project_name"] = project_name
                    project_details["project_manager_name"] = manager_name
                    projects_details.append(project_details)
            time.sleep(1)

        return projects_details

    def filtering_project_manager(self):
        drop_down_menu = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ant-dropdown-menu-vertical")))
        drop_down_menu_wait = WebDriverWait(drop_down_menu, 20)
        select_project_manger = drop_down_menu_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "li")))[1]
        select_project_manger.click()

    def get_projects_after_filtering(self):
        filtered_projects_details = []

        table = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))
        time.sleep(2)
        rows = table.find_elements(By.TAG_NAME, "tr")
        for index, row in enumerate(rows):
            project_details = {
                "project_name": "",
                "project_manager_name": ""
            }
            if index == 0:
                continue
            project_name = row.find_elements(By.TAG_NAME, "td")[0].text
            manager_cell = row.find_elements(By.TAG_NAME, "td")[-1]
            manager_name = manager_cell.find_elements(By.TAG_NAME, "span")[1].text
            project_details["project_name"] = project_name
            project_details["project_manager_name"] = manager_name
            filtered_projects_details.append(project_details)
            time.sleep(1)

        return filtered_projects_details

    def check_filter_work_correctly(self, p_manager_projects, p_filtered_projects):
        result = True
        if len(p_manager_projects) != len(p_filtered_projects):
            return False

        for item1, item2 in zip(p_manager_projects, p_filtered_projects):

            if item1 != item2:
                return False

        if result:
            print("Project manager filter is working")
        else:
            print("Project manager filter not working")

