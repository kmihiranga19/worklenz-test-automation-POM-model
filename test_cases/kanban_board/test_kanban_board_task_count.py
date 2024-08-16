from page_objects.KanbanBoard.KanbanBoardTaskCount import KanbanBoardTaskCount
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
        self.kb = KanbanBoardTaskCount(self.driver)
        self.kb.project_tab()
        self.kb.check_project_segment()
        self.kb.go_to_need_project_inside()
        self.kb.add_new_statues()
        self.kb.get_each_statues_tasks_count_before_adding_tasks()
        self.kb.get_all_statues()
        self.kb.add_tasks_to_boards()
        self.kb.get_each_statues_tasks_count_after_adding_tasks()
        self.kb.write_csv_file()