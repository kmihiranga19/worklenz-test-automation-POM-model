from selenium import webdriver
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class login:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enter_credentials(self, email, password):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Email']"))).send_keys(
            email)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']"))).send_keys(
            password)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Log in']"))).click()

    def Verify_user_able_login_with_correct_credentials(self):
        self.enter_credentials("ceyare4516@mliok.com", "ceyDigital#00")

        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "logo-holder")))

        except NoSuchElementException:
            pytest.fail("Test case fail: Verify user able login with correct credentials")

        self.driver.quit()

    def verify_unable_login_with_invalid_email(self):
        self.enter_credentials("ce4516.com", "ceyDigital#00")

        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[normalize-space()='Please input your email!']")))

        except NoSuchElementException:
            pytest.fail("Test case fail: Verify user able login with invalid email")

        self.driver.quit()

    def verify_unable_login_with_invalid_password(self):
        self.enter_credentials("ceyare4516@mliok.com", "")

        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[normalize-space()='Please input your Password!']")))

        except NoSuchElementException:
            pytest.fail("Test case fail: Verify user able login with invalid password")

        self.driver.quit()

    def verify_unable_login_with_wrong_credentials(self):
        self.enter_credentials("ceyare4516@mliok.com", "ceyDigital")

        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Log in']")))
        except NoSuchElementException:
            pytest.fail("Test case fail: Verify user able login with wrong password")

        self.driver.quit()
