import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def get_application_url(self):
        url = config.get('common data', 'baseURL')
        return url

    @staticmethod
    def get_email():
        email = config.get('common data', 'email')
        return email

    @staticmethod
    def get_password():
        password = config.get('common data', 'password')
        return password

    @staticmethod
    def get_inviteEmail():
        inviteEmail = config.get('common data', 'inviteEmail')
        return inviteEmail

    @staticmethod
    def get_userName():
        userName = config.get('common data', 'UserName')
        return userName
