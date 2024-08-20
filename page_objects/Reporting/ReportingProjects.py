from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import re
import csv
from datetime import datetime


class ReportingProjects:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(driver)
        self.owner_By_You_indexes = []
        self.tasks_time_estimated = []
        self.projects_details = []

    def go_to_project_tab(self):
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//strong[normalize-space()='Projects']"))).click()
        time.sleep(10)

    def open_team_selection(self):
        header = self.driver.find_element(By.TAG_NAME, "worklenz-header")
        header_2 = header.find_element(By.CLASS_NAME, "top-nav-ul-secondary")
        team_selection = header_2.find_elements(By.TAG_NAME, "li")[1]
        team_selection.click()
        time.sleep(5)

    def get_own_teams(self):
        self.open_team_selection()
        ul = self.driver.find_element(By.CLASS_NAME, "members-dropdown")
        teams = ul.find_elements(By.TAG_NAME, "li")
        for index, team in enumerate(teams):
            owner = team.find_element(By.TAG_NAME, "small")
            Owner_by = owner.text.strip()
            if Owner_by == "Owned by You":
                self.owner_By_You_indexes.append(index)

    def task_drawer_close(self):
        drawer_close = self.driver.find_element(By.XPATH,
                                                "//div[@class='ant-drawer ant-drawer-right ng-star-inserted ant-drawer-open']//span[@class='anticon anticon-close ng-star-inserted']//*[name()='svg']")
        drawer_close.click()
        time.sleep(2)

    def sub_task_drawers_close(self):
        self.driver.find_element(By.XPATH, "//button[@aria-label='Close']//div[1]").click()
        time.sleep(1)
        self.task_drawer_close()
        time.sleep(2)

    def get_task_estimated_time_hour(self):
        estimated_hour = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Hours']")))
        estimated_hour_value = estimated_hour.get_attribute("value")
        int_hour = int(estimated_hour_value)

        return int_hour

    def get_task_estimated_time_minitues(self):
        estimated_minitues = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Minutes']")))
        estimated_minitues_value = estimated_minitues.get_attribute("value")
        int_minitues = int(estimated_minitues_value)

        return int_minitues

    def get_time_logs(self):
        self.driver.find_element(By.XPATH, "//div[contains(text(),'Time Log')]").click()
        time_log = self.wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                     "//nz-skeleton/div/span")))
        time_log_str = time_log.text
        reg = re.search(r'(\d+)h (\d+)m', time_log_str)
        hour = int(reg.group(1))
        min = int(reg.group(2))
        time.sleep(1)

        return hour, min

    def pagination_count_change(self):
        pagination = self.driver.find_element(By.TAG_NAME, "nz-pagination")
        page_drop_down = pagination.find_elements(By.TAG_NAME, "li")[-1]
        page_drop_down.click()
        time.sleep(2)
        page_count = self.driver.find_elements(By.TAG_NAME, "nz-option-item")[2]
        time.sleep(1)
        page_count.click()
        time.sleep(2)

    def task_arrow_click(self):
        task_rows = self.driver.find_elements(By.TAG_NAME, "worklenz-task-list-row")
        for task_row in task_rows:
            task_arrow = task_row.find_element(By.CLASS_NAME, "task-arrow")
            span_tag = task_arrow.find_element(By.TAG_NAME, "span")
            class_name = span_tag.get_attribute("class")
            if "hidden-arrow" not in class_name:
                task_row.find_element(By.CLASS_NAME, "task-arrow").click()
        time.sleep(5)

    def get_project_last_activity(self):
        task_rows = self.driver.find_elements(By.TAG_NAME, "worklenz-task-list-row")
        task_name_container = task_rows[0].find_element(By.CLASS_NAME, "inner-task-name-container")
        self.actions.move_to_element(task_name_container).perform()
        open_btn = task_name_container.find_element(By.TAG_NAME, "button")
        open_btn.click()
        time.sleep(1)
        estimated_hour_input = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Hours']")))
        estimated_hour_input.send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        estimated_hour_input.send_keys("10")  # update estimated time to check project last activate
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[contains(text(),'Activity Log')]").click()
        time.sleep(3)
        time_table_content = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "ant-timeline-item-content")))
        owner_name = time_table_content.find_elements(By.TAG_NAME, "strong")[0].text
        self.task_drawer_close()
        time.sleep(3)
        return owner_name

    def get_project_update(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Updates']"))).click()
        time.sleep(3)
        comment = ""
        try:
            last_update_comment = self.driver.find_elements(By.TAG_NAME, "nz-comment")
            if len(last_update_comment) > 0:
                last_comment = last_update_comment[0]
                mention_text = last_comment.find_element(By.CLASS_NAME, "mention-text").text
                comment = mention_text
        except NoSuchElementException:
            print("no element")
            time.sleep(1)

        self.driver.find_element(By.XPATH, "//a[normalize-space()='Task List']").click()
        time.sleep(4)
        return comment

    def get_project_team(self):
        switch_team = self.driver.find_element(By.CLASS_NAME, "teams-switch")
        team_tag = switch_team.find_element(By.TAG_NAME, "strong")
        project_team = team_tag.text
        return project_team

    def get_days_left_overdue(self, end_date):
        left_overdue_days = ""
        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y-%m-%d")  # only get date without time as a string
        print(formatted_date)
        formatted_current_date = datetime.strptime(formatted_date, "%Y-%m-%d")  # string convert to daytime objects
        formatted_end_date = datetime.strptime(end_date, "%Y-%m-%d")
        _days = (formatted_end_date - formatted_current_date).days
        if _days > 0:
            _days_str = str(_days)
            left_overdue_days = _days_str + " days left"
        else:
            _days_str = str(_days)
            left_overdue_days = _days_str + " overdue"
        return left_overdue_days

    def get_each_task_details(self):
        estimated_hour = 0
        estimated_min = 0
        logged_hour = 0
        logged_min = 0
        self.task_arrow_click()
        task_rows = self.driver.find_elements(By.TAG_NAME, "worklenz-task-list-row")
        owner_name = self.get_project_last_activity()
        for task_row in task_rows:
            task_name_container = task_row.find_element(By.CLASS_NAME, "inner-task-name-container")
            self.actions.move_to_element(task_name_container).perform()
            open_btn = task_name_container.find_element(By.TAG_NAME, "button")
            open_btn.click()
            time.sleep(1)
            estimated_hour = estimated_hour + self.get_task_estimated_time_hour()
            estimated_min = estimated_min + self.get_task_estimated_time_minitues()
            time.sleep(1)
            log_hour, log_min = self.get_time_logs()
            logged_hour = logged_hour + log_hour
            logged_min = logged_min + log_min
            try:
                self.task_drawer_close()

            except NoSuchElementException:
                self.sub_task_drawers_close()

        cal_est_minitues = estimated_min / 60
        integer_part, fractional_part = divmod(cal_est_minitues, 1)
        integer_value = int(integer_part)
        float_value = fractional_part * 60
        float_value_to_round = round(float_value, 2)  # number round
        float_value_to_int = int(float_value_to_round)
        estimated_hour = estimated_hour + integer_value
        estimated_min = float_value_to_int

        cal_log_minitues = logged_min / 60
        integer_part, fractional_part = divmod(cal_log_minitues, 1)
        integer_value = int(integer_part)
        float_value = fractional_part * 60
        float_value_to_round = round(float_value, 2)  # number round
        float_value_to_int = int(float_value_to_round)
        logged_hour = logged_hour + integer_value
        logged_min = float_value_to_int
        tasks_details = {
            "total_estimated_hours": estimated_hour,
            "total_estimated_minutes": estimated_min,
            "total_logged_hours": logged_hour,
            "total_logged_minutes": logged_min,
            "last_activity": owner_name + " updated the estimation",

        }
        return tasks_details

    def get_project_details(self):
        left_overdue_date = ""
        project_team = self.get_project_team()
        project_update = self.get_project_update()
        tasks_details = self.get_each_task_details()
        self.driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
        page_header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "nz-page-header-title")))
        page_title = page_header.find_element(By.CLASS_NAME, "project-title")
        page_header = self.driver.find_element(By.TAG_NAME, "nz-page-header-extra")
        page_header.find_elements(By.CLASS_NAME, "ant-space-item")[2].click()
        time.sleep(3)
        status = self.driver.find_element(By.XPATH,
                                          "//nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-item")
        selected_status = status.get_attribute("title")
        start_date = self.driver.find_element(By.XPATH, "//div/div/nz-date-picker/div/input")
        selected_start_date = start_date.get_attribute("value")
        end_date = self.driver.find_element(By.XPATH,
                                            "//div[2]/nz-form-item/nz-form-control/div/div/nz-date-picker/div/input")
        selected_end_date = end_date.get_attribute("value")
        if selected_end_date != "":
            left_overdue_date = self.get_days_left_overdue(selected_end_date)
        health = self.driver.find_element(By.XPATH,
                                          "//nz-form-item[5]/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input")
        selected_health = health.get_attribute("value")
        category = self.driver.find_element(By.XPATH,
                                            "//nz-form-item[5]/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input")
        selected_category = category.get_attribute("value")
        client = self.driver.find_element(By.XPATH,
                                          "//worklenz-clients-autocomplete/form/nz-form-item/nz-form-control/div/div/input")
        selected_client = client.get_attribute("value")
        project_details = {
            "team": project_team,
            "project_name": page_title.text,
            "estimated_time_hour": tasks_details["total_estimated_hours"],
            "estimated_time_minutes": tasks_details["total_estimated_minutes"],
            "actual_time_hour": tasks_details["total_logged_hours"],
            "actual_time_minitues": tasks_details["total_logged_minutes"],
            "last_activity": tasks_details["last_activity"],
            "status": selected_status,
            "start_date": selected_start_date,
            "end_date": selected_end_date,
            "day_left_overdue": left_overdue_date,
            "project_health": selected_health,
            "category": selected_category,
            "project_update": project_update,
            "client": selected_client,

        }

        print(project_details)
        return project_details

    def get_projects_details(self):
        t_body = self.driver.find_element(By.TAG_NAME, "tbody")
        rows = t_body.find_elements(By.TAG_NAME, "tr")
        for index, row in enumerate(rows):
            self.pagination_count_change()
            t_body = self.driver.find_element(By.TAG_NAME, "tbody")
            rows = t_body.find_elements(By.TAG_NAME, "tr")
            rows[index].click()
            time.sleep(5)
            project_details = self.get_project_details()
            self.projects_details.append(project_details)
            self.driver.get("https://worklenz.com/worklenz/projects")
            time.sleep(5)

    def get_own_team_projects_details(self):
        for owner_by_you_index in self.owner_By_You_indexes:
            ul = self.driver.find_element(By.CLASS_NAME, "members-dropdown")
            teams = ul.find_elements(By.TAG_NAME, "li")
            teams[owner_by_you_index].click()
            time.sleep(6)
            self.get_projects_details()
            self.open_team_selection()

        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y_%m_%d_%H_%M_%S")
        csv_file_path = "projects" + formatted_time.strip() + ".csv"

        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)

            header_written = False
            for project_details in self.projects_details:
                if not header_written:
                    writer.writerow(project_details.keys())
                    header_written = True

                writer.writerow(project_details.values())
        return
