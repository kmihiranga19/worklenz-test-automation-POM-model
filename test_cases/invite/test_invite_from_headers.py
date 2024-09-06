from page_objects.Login.login import Login
from page_objects.Invite.InviteFromHeader import InviteFromHeader
import time
from utilities.readProperties import ReadConfig


class TestInviteProject:
    baseURL = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_invite_from_headers(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lg = Login(self.driver)
        self.lg.enter_email(self.email)
        self.lg.enter_password(self.password)
        self.lg.submit()
        self.ifH = InviteFromHeader(self.driver)
        self.ifH.header_team_invite_btn()
        self.invited_member = self.ifH.add_team_member()
        self.ifH.go_to_team_members_list()
        self.members_list = self.ifH.team_members_list()
        self.ifH.check_invited_member_add_to_list(self.invited_member, self.members_list)

