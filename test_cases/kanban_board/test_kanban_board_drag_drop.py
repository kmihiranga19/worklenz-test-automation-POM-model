from page_objects.KanbanBoard.KanbanBoardDragDrop import KanbanBoardDragDrop
from page_objects.Login.login import Login
from utilities.readProperties import ReadConfig


class TestKanbanBoard:
    baseURL = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_kanban_board_drag_drop(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = Login(self.driver)
        self.lg.enter_email(self.email)
        self.lg.enter_password(self.password)
        self.lg.submit()
        self.kb = KanbanBoardDragDrop(self.driver)
        self.kb.project_tab()
        self.kb.check_project_segment()
        self.kb.go_to_need_project_inside()
        self.kb.before_get_doing_status_tasks()
        self.kb.before_get_done_status_tasks()
        self.kb.task_drag_and_drop()
        self.kb.after_get_doing_status_tasks()
        self.kb.after_get_done_status_tasks()
        self.kb.write_doing_CSV1()
        self.kb.write_doing_CSV2()





        



