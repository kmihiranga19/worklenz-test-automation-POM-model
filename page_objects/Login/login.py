from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.BasePage import Basepage
from page_objects.Locators import LoginLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Email']"))).send_keys(
            email)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']"))).send_keys(password)

    def submit(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Log in']"))).click()
