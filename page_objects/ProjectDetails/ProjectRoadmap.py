from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects.BasePage import Basepage
from page_objects.Locators import ProjectRoadmapLocators


class ProjectRoadmap(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = ProjectRoadmapLocators()

    def clickProjectTab(self):
        self.element_click("project_tab_xpath", self.locators.project_tab_xpath)

    def selectProject(self):
        self.element_click("select_project_xpath", self.locators.select_project_xpath)

    def clickRoadMap(self):
        self.element_click("roadmap_tab_xpath", self.locators.roadmap_tab_xpath)
