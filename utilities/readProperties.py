import configparser
import os

config = configparser.RawConfigParser()
config_file_path = os.path.join(os.path.dirname(__file__), "..", "Configurations", "config.ini")
config.read(config_file_path)


class ReadConfig:


    @staticmethod
    def get_application_url():
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
