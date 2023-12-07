from page_objects.Login.login import Login
from page_objects.TeamsSelection.TeamSelection import TeamSelection
import time
from utilities.readProperties import ReadConfig
from self import self


class TestTeamSelection:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_team_selection(self, setup):
        self.browser = setup
        self.browser.get(self.baseURL)
        self.lg = Login(self.browser)
        time.sleep(3)
        self.lg.clickLogin()
        time.sleep(3)
        self.lg.setEmail(self.email)
        self.lg.setpassword(self.password)
        time.sleep(3)
        self.lg.submit()
        time.sleep(3)
        self.ts = TeamSelection(self.browser)
        time.sleep(3)
        self.ts.clickTeamSelection()
        time.sleep(3)
        self.ts.clickSelectTeam()
        time.sleep(3)
        self.ts.clickTeamSelection2()
        time.sleep(3)
        self.ts.clickSelectTeam2()
        time.sleep(5)