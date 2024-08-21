import time

import pytest

from page_objects.CustomTemplate.CustomTemplate import CustomTemplate
from page_objects.Login.login import Login
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By


class TestCustomTemplates:
    base_url = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_custom_template(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lg = Login(self.driver)
        self.lg.enter_email(self.email)
        self.lg.enter_password(self.password)
        self.lg.submit()
        time.sleep(3)
        self.ct = CustomTemplate(self.driver)
        self.ct.go_to_projects_tab()
        self.ct.check_project_availability()
        self.ct.tasks_information_saved_successfully()