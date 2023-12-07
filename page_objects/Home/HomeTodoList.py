from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from page_objects.BasePage import Basepage
from page_objects.Locators import HomeTodoListLocators


class HomeTodoList(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = HomeTodoListLocators()

    def enterToDoTask(self, todoTask):
        self.enter_task(todoTask,"to_do_input_xpath",self.locators.to_do_input_xpath)

    def clickRefreshBtn(self):
        self.element_click("refresh_Btn_xpath", self.locators.refresh_Btn_xpath)

    def clickDoneBtn(self):
        self.element_click("to_do_task_done_xpath", self.locators.to_do_task_done_xpath)
