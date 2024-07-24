from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Basepage:
    def __init__(self, browser):
        self.browser = browser

    def get_element(self, locator_name, locator_value):
        element = None
        if locator_name.endswith("_id"):
            element = self.browser.find_element(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            element = self.browser.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_class_name"):
            element = self.browser.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            element = self.browser.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_xpath"):
            element = self.browser.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_css"):
            element = self.browser.find_element(By.CSS_SELECTOR, locator_value)
        elif locator_name.endswith("_tag"):
            element = self.browser.find_element(By.TAG_NAME,locator_value)
        return element

    def element_click(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()

    def enter_input_name(self, text, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        element.send_keys(text)

    def enter_admin_center_overview(self, text, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(text + Keys.ENTER)

    def enter_search_filed(self,text, locator_name, locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def enter_client_input(self,text,locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.send_keys(text + Keys.ENTER + Keys.ENTER)

    def enter_invite_email(self, text, locator_name, locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.send_keys(text + Keys.ENTER)

    # def enter_login_email(self,text, locator_name,locator_value):
    #     element = self.get_element(locator_name, locator_value)
    #     element.clear()
    #     element.send_keys(text)
    #
    # def enter_login_password(self,text,locator_name,locator_value):
    #     element = self.get_element(locator_name,locator_value)
    #     element.send_keys(text)

    def set_timelog(self, text,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()
        time.sleep(2)
        element.send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        element.send_keys(Keys.BACKSPACE + text)

    def enter_description_link(self,text,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        element.send_keys(text)

    def enter_subTask(self,text,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.send_keys(text, Keys.ENTER)

    def get_date_picker(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        element.click()

    def enter_renamePhase(self,text,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        element.send_keys(text + Keys.ENTER)

    def enter_task(self,text,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.send_keys(text + Keys.ENTER)

    def home_enter_task(self,text,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.send_keys(text,Keys.TAB)

















