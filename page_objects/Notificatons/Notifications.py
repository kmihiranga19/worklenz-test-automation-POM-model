from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.BasePage import Basepage
from page_objects.Locators import NotificationsLocators


class Notifications(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = NotificationsLocators()

    def clickNotificationsIcon(self):
        self.element_click("notification_icon_xpath", self.locators.notification_icon_xpath)

    def clickMarkRead(self):
        self.element_click("mark_as_read_xpath", self.locators.mark_as_read_xpath)

    def clickReadBtn(self):
        self.element_click("read_button_xpath", self.locators.read_button_xpath)

    def clickUnreadBtn(self):
        self.element_click("unread_btn_xpath", self.locators.unread_btn_xpath)

    def clickMarkAllRead(self):
        self.element_click("mark_all_as_read_xpath",self.locators.mark_all_as_read_xpath)

    def clickJoinBtn(self):
        self.element_click("join_btn_xpath", self.locators.join_btn_xpath)

    def clickCloseBtn(self):
        self.element_click("close_btn_xpath", self.locators.close_btn_xpath)

