from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from page_objects.BasePage import Basepage
from page_objects.Locators import HomeProjectLocators


class HomeProject(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = HomeProjectLocators()

    def clickRefreshBtn(self):
        self.element_click("refresh_btn_xpath", self.locators.refresh_btn_xpath)

    def clickStar(self):
        self.element_click("star_xpath", self.locators.star_xpath)

    def clickFavTab(self):
        self.element_click("fav_tab_xpath", self.locators.fav_tab_xpath)

    def clickRecentTab(self):
        self.element_click("recent_xpath", self.locators.recent_xpath)

    def clickProject(self):
        self.element_click("project_xpath",self.locators.project_xpath)



