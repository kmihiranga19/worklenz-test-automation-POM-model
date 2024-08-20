import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from faker import Faker


class TimeLog:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.faker = Faker()

    def go_to_project_tab(self):
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//strong[normalize-space()='Projects']"))).click()
        time.sleep(10)

    def team_select(self):
        header = self.driver.find_element(By.TAG_NAME, "worklenz-header")
        header_2 = header.find_element(By.CLASS_NAME, "top-nav-ul-secondary")
        team_selection = header_2.find_elements(By.TAG_NAME, "li")[1]
        team_selection.click()
        time.sleep(5)
        ul = self.driver.find_element(By.CLASS_NAME, "members-dropdown")
        team = ul.find_elements(By.TAG_NAME, "li")[-1]
        team.click()
        time.sleep(2)

    def select_page_counter(self):
        pagination = self.driver.find_element(By.TAG_NAME, "nz-pagination")
        page_drop_down = pagination.find_elements(By.TAG_NAME, "li")[-1]
        page_drop_down.click()
        time.sleep(2)
        page_count = self.driver.find_elements(By.TAG_NAME, "nz-option-item")[2]
        page_count.click()
        time.sleep(2)

    def enter_time_log(self):
        hour = self.faker.random_int(min=0, max=9)
        minutes = self.faker.random_int(min=0, max=60)
        seconds = self.faker.random_int(min=0, max=100)
        t_body = self.driver.find_element(By.TAG_NAME, "tbody")
        rows = t_body.find_elements(By.TAG_NAME, "tr")
        for index in range(len(rows)):
            t_body = self.driver.find_element(By.TAG_NAME, "tbody")
            rows = t_body.find_elements(By.TAG_NAME, "tr")
            rows[index].click()
            time.sleep(3)
            tasks = self.driver.find_element(By.CLASS_NAME, "task-name-text")
            tasks.click()
            time.sleep(1)
            task_inner = self.driver.find_element(By.CLASS_NAME, "inner-task-name-container")
            task_open = task_inner.find_element(By.TAG_NAME, "button")
            task_open.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[contains(text(),'Time Log')]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//span[normalize-space()='Add Timelog']").click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//input[@placeholder='Hours']").send_keys(hour)
            self.driver.find_element(By.XPATH, "//input[@placeholder='Minutes']").send_keys(minutes)
            self.driver.find_element(By.XPATH, "//input[@placeholder='Seconds']").send_keys(seconds)
            self.driver.find_element(By.XPATH, "//span[normalize-space()='Log time']").click()
            time.sleep(2)
            self.driver.get("https://uat.worklenz.com/worklenz/projects")
            time.sleep(5)
            self.select_page_counter()
            time.sleep(3)

        pagination = self.driver.find_element(By.TAG_NAME, "nz-pagination")
        next_btn = pagination.find_element(By.CLASS_NAME, "ant-pagination-next")
        button = next_btn.find_element(By.TAG_NAME, "button")
        if button.is_enabled():
            next_btn.click()
            time.sleep(5)
            self.enter_time_log()

        return

