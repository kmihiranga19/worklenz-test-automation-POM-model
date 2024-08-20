from page_objects.TimeLog.TimeLog import TimeLog
from page_objects.Login.login import Login
from utilities.readProperties import ReadConfig


class TestKanbanBoard:
    baseURL = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_kanban_board_drag_drop(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = Login(self.driver)
        self.lg.enter_email(self.email)
        self.lg.enter_password(self.password)
        self.lg.submit()
        self.tg = TimeLog(self.driver)
        self.tg.go_to_project_tab()
        self.tg.team_select()
        self.tg.select_page_counter()
        self.tg.enter_time_log()