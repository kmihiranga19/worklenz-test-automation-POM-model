from selenium.webdriver.common.by import By
from page_objects.BasePage import Basepage
from page_objects.Locators import SignUpLocators, InviteOnboardingLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time


class Signup_Onboarding(Basepage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.fake = Faker()
        self.task_names = ["Planning", "Designing", "Coding", "Testing", "Maintaining", "Release"]

    def signUp(self):
        random_name = self.fake.name()
        random_email = self.fake.email()
        self.wait.until(EC.visibility_of_element_located((By.ID, "full-name"))).send_keys(random_name)
        self.wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(random_email)
        self.wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("ceyDigital#00")
        # form = self.driver.find_element(By.TAG_NAME, "form")
        # form_wait = WebDriverWait(form, 10)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Sign up']"))).click()
        time.sleep(2)

    def give_organization_name(self):
        random_org_name = self.fake.name()
        organization = random_org_name + " Team"
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "input"))).send_keys(organization)
        continue_btn = self.driver.find_element(By.TAG_NAME, "button")
        if continue_btn.is_enabled():
            continue_btn.click()
            time.sleep(2)
        else:
            print("Please enter valid organization name")
        return organization

    def create_first_project(self):
        project = self.fake.random_element(elements=('A', 'B', 'C', 'D'))
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "input"))).send_keys(
            "First project" +
            project)
        input_element = self.driver.find_element(By.TAG_NAME, "input")
        first_project_name = input_element.get_attribute("value")
        continue_btn = self.driver.find_element(By.XPATH, "//span[normalize-space()='Continue']")
        continue_btn.click()
        time.sleep(5)
        return first_project_name.strip()

    def create_first_tasks(self):
        add_another_task = self.driver.find_element(By.XPATH, "//span[normalize-space()='Add another']")
        continue_btn = self.driver.find_element(By.XPATH, "//span[normalize-space()='Continue']")

        i = 0

        while i < 5:
            add_another_task.click()
            i += 1

        time.sleep(3)

        for i in range(6):
            element = self.driver.find_element(By.ID, f"task-name-input-{i}")
            element.send_keys(self.task_names[i])

        time.sleep(2)
        continue_btn.click()

    def invite_team_members(self):
        add_another_task = self.driver.find_element(By.XPATH, "//span[normalize-space()='Add another']")
        continue_btn = self.driver.find_element(By.XPATH, "//span[normalize-space()='Continue']")

        i = 0

        while i < 2:
            add_another_task.click()
            i += 1

        menu = self.driver.find_element(By.TAG_NAME, "nz-list")
        inputs = menu.find_elements(By.TAG_NAME, "input")

        for i in range(3):
            random_email = self.fake.email()
            inputs[i].send_keys(random_email)

        if continue_btn.is_enabled():
            continue_btn.click()
            time.sleep(3)

        else:
            print("Please enter valid Email address")

        time.sleep(10)

    def skip_invite_team_members(self):
        skip_btn = self.driver.find_element(By.CSS_SELECTOR, "span[class='ant-typography']")
        skip_btn.click()

    def get_organization_name(self):
        header = self.driver.find_element(By.TAG_NAME, "worklenz-header")
        header_2 = header.find_element(By.CLASS_NAME, "top-nav-ul-secondary")
        team_selection = header_2.find_elements(By.TAG_NAME, "li")[1]
        team_selection.click()
        time.sleep(1)
        team_selection_items = self.driver.find_element(By.CLASS_NAME, "align-items-baseline")
        team = team_selection_items.find_elements(By.TAG_NAME, "span")[0]
        organization_text = team.text.strip()
        return organization_text

    def get_project_name(self):
        page_header_title = self.driver.find_element(By.TAG_NAME, "nz-page-header-title")
        project_title = page_header_title.find_element(By.CLASS_NAME, "project-title")
        project_text = project_title.text.strip()
        return project_text

    def get_project_tasks(self):
        tasks = []
        task_rows = self.driver.find_elements(By.TAG_NAME, "worklenz-task-list-row")
        for task_row in task_rows:
            task_name = task_row.find_element(By.CLASS_NAME, "task-name-text")
            tasks.append(task_name.text.strip())

        return tasks

    def check_organization_name(self, org_name, created_org_name):
        if created_org_name == org_name:
            print("Organization successfully created")

        else:
            print("Your entered organization not created")

    def check_project_name(self, first_project_name, created_first_project_name):
        if created_first_project_name == first_project_name:
            print("First project successfully created")

        else:
            print("Your entered project not created")

    def check_project_tasks(self, created_tasks):
        if len(self.task_names) == len(created_tasks):
            for created_task in created_tasks:
                if created_task in self.task_names:
                    print(created_task + " task successfully created")

                else:
                    print(created_task + " task not created")
