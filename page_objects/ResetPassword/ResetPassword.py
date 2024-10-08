import time
from faker import Faker
from selenium import webdriver
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class ResetPassword:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.faker = Faker()
        self.no = self.faker.random_int()

    def account_log_out(self):
        wl_header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "worklenz-header")))
        wl_header_wait = WebDriverWait(wl_header, 20)
        left_header = wl_header_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "top-nav-ul-secondary")))
        left_header_wait = WebDriverWait(left_header, 20)
        left_header_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "li")))[-1].click()
        # drop_down = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "profile-details-dropdown")))
        # drop_down_wait = WebDriverWait(drop_down, 20)
        # drop_down_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "li")))[2].click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='OK']"))).click()

    def forgot_password_process(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-form-forgot"))).click()
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'input'))).send_keys(Keys.CONTROL + 'v')
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Reset Password']"))).click()

    def create_new_user_account(self):
        self.driver.get("https://temp-mail.org/en/")
        time.sleep(10)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[id='click-to-copy']"))).click()
        self.driver.back()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='full-name']"))).send_keys(
            "Test_user")
        email = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='email']")))
        email.send_keys(Keys.CONTROL + 'v')
        created_account_email = email.get_attribute('value')
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='password']"))).send_keys(
            "ceyDigital#00")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Sign up']"))).click()
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input"))).send_keys("project")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Continue']"))).click()
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Import from templates']"))).click()
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//button[@class='ant-btn ant-btn-primary'])"))).click()

        return created_account_email

    def verify_user_account_created(self, created_email):
        wl_header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "worklenz-header")))
        wl_header_wait = WebDriverWait(wl_header, 20)
        left_header = wl_header_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "top-nav-ul-secondary")))
        left_header_wait = WebDriverWait(left_header, 20)
        left_header_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "li")))[-1].click()
        account_name = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "account-name")))
        account_name_wait = WebDriverWait(account_name, 20)
        account_owner_email = account_name_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'p')))[0].text
        if account_owner_email.strip() == created_email.strip():
            pass
        else:
            pytest.fail("Created account has something wrong")

    def test_verify_reset_password_work(self):
        created_email = self.create_new_user_account()
        self.verify_user_account_created(created_email)
        self.account_log_out()
        self.forgot_password_process()
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[normalize-space()='Reset instruction sent!']")))
        except NoSuchElementException:
            pytest.fail("Test case fail: test_verify_reset_password_work")
        finally:
            self.driver.quit()
