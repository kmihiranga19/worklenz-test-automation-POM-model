from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from page_objects.BasePage import Basepage
from page_objects.Locators import SettingsNotificationsLocators


class SettingsNotifications(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = SettingsNotificationsLocators()

    def clickNotificationsTab(self):
        self.element_click("notifications_tab_xpath", self.locators.notifications_tab_xpath)

    def clickEmailNotifications(self):
        self.element_click("email_notifications_xpath", self.locators.email_notifications_xpath)

    def clickDailyDigest(self):
        self.element_click("daily_digest_xpath", self.locators.daily_digest_xpath)

    def clickPushNotifications(self):
        self.element_click("push_notifications_xpath", self.locators.push_notifications_xpath)

    def clickUnreadItem(self):
        self.element_click("unread_items_xpath", self.locators.unread_items_xpath)
