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


class CustomTemplate:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.singleTask = {
            "name": "",
            "status": "",
            "priority": "",
            "phase": "",
            "time_estimation": ""}
        self.taskInfo = []
        self.customSaveTaskInfo = []

    def go_to_projects_tab(self):
        self.driver.get("https://uat.app.worklenz.com/worklenz/projects")
        time.sleep(5)

    def check_need_tasksList_fields_visible(self):
        show_fields = self.wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "worklenz-task-list-columns-toggle")))
        show_fields_wait = WebDriverWait(show_fields, 10)
        show_fields_wait.until(EC.visibility_of_element_located((By.TAG_NAME, "button"))).click()
        drop_down_menu = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cdk-overlay-connected-position-bounding-box")))
        drop_down_menu_wait = WebDriverWait(drop_down_menu, 10)
        drop_main = drop_down_menu_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "div")))[1]
        drop_main_wait = WebDriverWait(drop_main, 10)
        items = drop_main_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "li")))
        phase_field = items[-1].get_attribute("class")
        time_estimated_field = items[8].get_attribute("class")
        included_class_name = r'\bant-checkbox-wrapper-checked\b'
        check_phase_class_name = re.search(included_class_name, phase_field)
        check_estimated_class_name = re.search(included_class_name, time_estimated_field)

        if check_phase_class_name:
            print("Phase field already checked")

        else:
            items[-1].click()

        if check_estimated_class_name:
            print("Time estimated already checked")

        else:
            items[8].click()

        self.driver.find_element(By.XPATH, "//label[normalize-space()='Group by:']").click()

    def create_project_tasks(self):
        fake = Faker()
        taskList = self.driver.find_element(By.CLASS_NAME, "tasks-wrapper")
        add_task_bts = taskList.find_elements(By.CLASS_NAME, "editable-row")
        for add_task_bt in add_task_bts:
            add_task_bt.click()
            time.sleep(1)
            random_task_name = fake.catch_phrase()
            self.driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Type your task and hit enter']").send_keys(
                random_task_name + Keys.ENTER)
            time.sleep(2)

    def get_tasks_data(self):
        task_list = self.driver.find_element(By.CLASS_NAME, "tasks-wrapper")
        tasksRow = task_list.find_elements(By.TAG_NAME, "worklenz-task-list-row")
        for taskRow in tasksRow:
            task_name = taskRow.find_element(By.CLASS_NAME, "task-name-text")
            status_cell = taskRow.find_element(By.TAG_NAME, "worklenz-task-list-status")
            status = status_cell.find_element(By.TAG_NAME, "nz-select-item")
            priority_cell = taskRow.find_element(By.TAG_NAME, "worklenz-task-list-priority")
            priority = priority_cell.find_element(By.TAG_NAME, "nz-select-item")
            phases_cell = taskRow.find_element(By.TAG_NAME, "worklenz-task-list-phase")
            try:
                phase = phases_cell.find_element(By.TAG_NAME, "nz-select-item")
                phase_text = phase.text

            except NoSuchElementException:
                phase_text = ""

            estimated_time_cell = taskRow.find_element(By.CLASS_NAME, "task-estimation")
            estimated_time = estimated_time_cell.find_element(By.CLASS_NAME, "task-due-label")

            self.singleTask["name"] = task_name.text
            self.singleTask["status"] = status.text
            self.singleTask["priority"] = priority.text
            self.singleTask["phase"] = phase_text
            self.singleTask["time_estimation"] = estimated_time.text

            self.taskInfo.append(self.singleTask.copy())

    def save_custom_template(self):
        fake = Faker()
        random_tem_name = fake.name()
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        header_bts = self.driver.find_element(By.TAG_NAME, "nz-page-header-extra")
        temp_save_btn = header_bts.find_elements(By.TAG_NAME, "button")[1]
        temp_save_btn.click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter template name"]').send_keys(Keys.ENTER)
        temp_name = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter template name"]')
        temp_name.send_keys(random_tem_name)
        entered_value = temp_name.get_attribute("value")
        entered_value.strip()
        time.sleep(1)
        save_btn = self.driver.find_element(By.CSS_SELECTOR,
                                            "div[class='ant-drawer ant-drawer-right ng-star-inserted ant-drawer-open'] button[class='ant-btn ant-btn-primary'] span[class='ng-star-inserted']")
        save_btn.click()
        time.sleep(5)
        return entered_value

    def go_to_saved_custom_template(self):
        wl_header = self.driver.find_element(By.TAG_NAME, "worklenz-header")
        left_header = wl_header.find_elements(By.TAG_NAME, "ul")[2]
        profile_icon = left_header.find_elements(By.TAG_NAME, "li")[-1]
        profile_icon.click()
        time.sleep(1)
        drop_down_menu = self.driver.find_element(By.CSS_SELECTOR,
                                                  "ul[class='ant-menu ant-menu-root ant-menu-light ant-menu-vertical']")
        drop_down_menu.find_elements(By.TAG_NAME, "li")[1].click()
        time.sleep(5)
        settings_side_bar = self.driver.find_element(By.TAG_NAME, "nz-sider")
        project_temp_tab = settings_side_bar.find_elements(By.TAG_NAME, "li")[6]
        project_temp_tab.click()
        time.sleep(6)

    def edit_saved_custom_template(self, temp_name: str):
        table = self.driver.find_element(By.TAG_NAME, "tbody")
        table_rows = table.find_elements(By.TAG_NAME, "tr")
        row_index = -1
        for index, table_row in enumerate(table_rows):
            saved_tem_name = table_row.find_elements(By.CLASS_NAME, "ant-table-cell")[0]
            if temp_name == saved_tem_name.text.strip():
                row_index = index
                break
        if row_index > -1:
            edit_btn = table_rows[row_index].find_elements(By.TAG_NAME, "button")[0]
            edit_btn.click()

        else:
            print("saved template not found")
            pagination = self.driver.find_element(By.TAG_NAME, "nz-pagination")
            next_btn = pagination.find_element(By.CLASS_NAME, "ant-pagination-next")
            if next_btn.is_enabled():
                next_btn.click()
                time.sleep(2)
                self.edit_saved_custom_template(temp_name)
            else:
                print("not found")
        return

    def get_saved_custom_project_data(self):
        table = self.driver.find_element(By.CLASS_NAME, "tasks-wrapper")
        tasks_rows = table.find_elements(By.TAG_NAME, "worklenz-pt-task-list-row")
        for task_row in tasks_rows:
            task_name = task_row.find_element(By.CLASS_NAME, "task-name-text")
            phase_cell = task_row.find_element(By.TAG_NAME, "worklenz-task-phase")
            try:
                phase = phase_cell.find_element(By.TAG_NAME, "nz-select-item")
                phase_text = phase.text

            except NoSuchElementException:
                phase_text = ""

            statues_cell = task_row.find_element(By.TAG_NAME, "worklenz-task-status")
            statues = statues_cell.find_element(By.TAG_NAME, "nz-select-item")
            priority_cell = task_row.find_element(By.TAG_NAME, "worklenz-task-priority")
            priority = priority_cell.find_element(By.TAG_NAME, "nz-select-item")
            time_estimated_cell = task_row.find_element(By.TAG_NAME, "worklenz-task-estimation")
            time_estimated = time_estimated_cell.find_element(By.TAG_NAME, "p")

            self.singleTask["name"] = task_name.text
            self.singleTask["status"] = statues.text
            self.singleTask["priority"] = priority.text
            self.singleTask["phase"] = phase_text
            self.singleTask["time_estimation"] = time_estimated.text

            self.customSaveTaskInfo.append(self.singleTask.copy())

    def check_project_availability(self):
        project_tabel = self.driver.find_element(By.TAG_NAME, "table")
        table_body = project_tabel.find_element(By.TAG_NAME, "tbody")
        table_rows = table_body.find_elements(By.CLASS_NAME, "actions-row")
        if len(table_rows) > 0:
            table_rows[4].click()
            self.check_need_tasksList_fields_visible()
            self.create_project_tasks()
            self.get_tasks_data()
            saved_value = self.save_custom_template()
            self.go_to_saved_custom_template()
            self.edit_saved_custom_template(saved_value)
            self.get_saved_custom_project_data()

        else:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Create Project')]"))).click()

    def tasks_information_saved_successfully(self):
        for task in self.taskInfo:
            # print(task)

            if task in self.customSaveTaskInfo:
                print(task["name"], "Task's information Saved successfully")

            else:
                print(task["name"], "Task's information Not saved successfully")

        time.sleep(10)
