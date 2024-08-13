import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import re
import csv


class KanbanBoard:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.fake = Faker()
        self.statues = []
        self.status_names = ["Backlog", "Ongoing", "Development work", "Testing & Review", "Resolved"]
        self.before_statues_details = []
        self.after_statues_details = []

    def project_tab(self):
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//strong[normalize-space()='Projects']"))).click()
        time.sleep(10)

    def check_project_segment(self):
        segments = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ant-segmented-group")))
        all_segment = segments.find_elements(By.TAG_NAME, "label")[0]
        all_segment_class_name = all_segment.get_attribute("class")
        if "item-selected" not in all_segment_class_name:
            all_segment.click()

    def go_to_need_project_inside(self):
        t_body = self.driver.find_element(By.TAG_NAME, "tbody")
        t_body.find_elements(By.TAG_NAME, "tr")[0].click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Board']"))).click()

    def add_new_statues(self):
        new_status_column = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "new-column-sec")))
        new_status_column.find_element(By.TAG_NAME, "button").click()
        status_name = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Name']")))
        status_name.send_keys(self.status_names[self.fake.random_int(min=0, max=4)])
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Create']").click()
        time.sleep(3)

    def get_each_statues_tasks_count_before_adding_tasks(self):
        board_wrapper = self.driver.find_element(By.CLASS_NAME, "board-wrapper")
        columns = board_wrapper.find_elements(By.CLASS_NAME, "board-column")
        for column in columns:
            status_details = {
                "status_title": "",
                "tasks_count": ""
            }
            status_label = column.find_element(By.CLASS_NAME, "kanban-status-label").text
            status_name = re.sub(r'\(\d+\)', '', status_label)
            tasks = column.find_elements(By.CLASS_NAME, "task")
            tasks_count = (len(tasks))
            status_details["status_title"] = status_name
            status_details["tasks_count"] = tasks_count
            self.before_statues_details.append(status_details)
        print(self.before_statues_details)
        return

    def get_all_statues(self):
        wrapper = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "board-wrapper")))
        statues_columns = wrapper.find_elements(By.CLASS_NAME, "board-column")
        for statues_column in statues_columns:
            self.statues.append(statues_column)
        time.sleep(3)

    def add_tasks_to_boards(self):
        i = 1
        while i <= len(self.statues):
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "(//div[@class='column-footer'])[" + str(i) + "]"))).click()
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter task name']"))).send_keys(
                self.fake.name(), "'s task" + Keys.ENTER)
            self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='ant-btn add-task-btn-card me-2']"))).click()
            i += 1

    def get_each_statues_tasks_count_after_adding_tasks(self):
        board_wrapper = self.driver.find_element(By.CLASS_NAME, "board-wrapper")
        columns = board_wrapper.find_elements(By.CLASS_NAME, "board-column")
        for column in columns:
            status_details = {
                "status_title": "",
                "tasks_count": ""
            }
            status_label = column.find_element(By.CLASS_NAME, "kanban-status-label").text
            status_name = re.sub(r'\(\d+\)', '', status_label)
            tasks = column.find_elements(By.CLASS_NAME, "task")
            tasks_count = (len(tasks))
            status_details["status_title"] = status_name
            status_details["tasks_count"] = tasks_count
            self.after_statues_details.append(status_details)
        print(self.after_statues_details)
        return

    def write_csv_file(self):
        file_path = 'check_tasks_count.csv'
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.before_statues_details[0].keys())
            writer.writeheader()
            writer.writerows(self.before_statues_details)
            writer.writerow({})
            writer.writerows(self.after_statues_details)




