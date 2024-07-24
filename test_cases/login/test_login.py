from page_objects.Login.userLogin import login
from utilities.readProperties import ReadConfig


class TestLogin:
    baseURL = ReadConfig.get_application_url()

    def test_verify_user_able_login_with_correct_credentials(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = login(self.driver)
        self.lg.Verify_user_able_login_with_correct_credentials()

    def test_verify_unable_login_with_invalid_email(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = login(self.driver)
        self.lg.Verify_user_able_login_with_correct_credentials()

    def test_verify_unable_login_with_invalid_password(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = login(self.driver)
        self.lg.verify_unable_login_with_invalid_password()

    def test_verify_unable_login_with_wrong_credentials(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = login(self.driver)
        self.lg.verify_unable_login_with_wrong_credentials()

