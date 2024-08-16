import time

import pytest

from page_objects.ImportTemplate.ImportingTemplate import ImportingTemplate
from page_objects.Login.login import Login
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By


class TestImportingTemplate:
    base_url = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_importing_template(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lg = Login(self.driver)
        self.lg.enter_email(self.email)
        self.lg.enter_password(self.password)
        self.lg.submit()
        time.sleep(3)
        self.it = ImportingTemplate(self.driver)
        self.it.go_to_projects()
        self.expected_URL = "https://uat.app.worklenz.com/worklenz/projects"
        self.current_URL = self.driver.current_url
        print(self.current_URL)
        if self.expected_URL == self.current_URL:
            print("Projects tab page is loaded")
            self.it.go_to_project_temp()
            self.it.get_need_temp()
            self.it.get_template_data()
            self.createBtn = self.driver.find_element(By.CSS_SELECTOR,
                                                      "button[class='ant-btn ant-btn-primary'] span[class='ng-star-inserted']")
            self.createBtn.click()
            self.it.check_data_import_correctly()
            time.sleep(3)

        else:
            print("Projects tab page not loaded")
            pytest.fail("Not redirect to relevant page")
