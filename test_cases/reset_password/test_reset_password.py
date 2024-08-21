import time

import pytest

from page_objects.ResetPassword.ResetPassword import ResetPassword
from page_objects.Login.login import Login
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By


class TestResetPassword:
    base_url = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_reset_password(self, setup):
        self.driver = setup
        self.driver.get("https://uat.app.worklenz.com/auth/signup")
        self.rp = ResetPassword(self.driver)
        self.rp.test_verify_reset_password_work()
