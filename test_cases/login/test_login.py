from page_objects.Login.userLogin import login
from utilities.readProperties import ReadConfig

class TestLogin:
    baseURL = ReadConfig.get_application_url()

    def test_(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = login
        self.lg.

