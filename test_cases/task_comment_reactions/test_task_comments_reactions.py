from typing import Any

from selenium.webdriver.chrome.webdriver import WebDriver

from utilities.readProperties import ReadConfig
from page_objects.Login.login import Login
from page_objects.TaskComments.TaskCommentsReactions import TaskCommentsReactions


class TestCommentsReactions:
    base_url = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_check_whether_user_able_to_react_the_comment(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lg = Login(self.driver)
        self.lg.enter_email(self.email)
        self.lg.enter_password(self.password)
        self.lg.submit()
        self.cr = TaskCommentsReactions(self.driver)
        self.cr.go_task_comment_section()
        self.cr.check_whether_user_able_to_react_the_comment()

    def test_check_whether_user_able_to_react_another_member_comment(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lg = Login(self.driver)
        self.lg.enter_email(self.email)
        self.lg.enter_password(self.password)
        self.lg.submit()
        self.cr = TaskCommentsReactions(self.driver)
        self.cr.go_task_comment_section()
        self.cr.check_whether_user_able_to_react_another_member_comment()

    def test_check_whether_user_able_to_remove_reaction_on_comment(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lg = Login(self.driver)
        self.lg.enter_email(self.email)
        self.lg.enter_password(self.password)
        self.lg.submit()
        self.cr = TaskCommentsReactions(self.driver)
        self.cr.go_task_comment_section()
        self.cr.check_whether_user_able_to_remove_reaction_on_comment()




