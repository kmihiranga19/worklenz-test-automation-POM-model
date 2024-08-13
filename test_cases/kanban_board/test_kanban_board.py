from page_objects.KanbanBoard.KanbanBoard import KanbanBoard
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
        self.kb = KanbanBoard
        self.kb.project_tab()
        



