import time
import pytest
from page_objects.SettingsChangePassword.SettingsChangePassword import SettingsChangePassword
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By


class TestResetPassword:
    base_url = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_reset_password(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.sp = SettingsChangePassword(self.driver)
        self.sp.test_verify_change_password_page()
        self.sp.test_verify_user_able_change_password()
        self.sp.test_verify_user_unable_change_psw_with_invalid_current_psw()
        self.sp.test_verify_user_unable_change_psw_with_invalid_confirm_new_psw()

