from configparser import ConfigParser

config = ConfigParser()
config.read(r'..\Configuration\config.ini')


class ReadConfig:

    print(">> " + str(config.sections()))

    @staticmethod
    def get_url():
        url = config.get('common info', 'url')
        return url

    @staticmethod
    def get_username():
        user = config.get('common info', 'username')
        return user

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_username_input():
        username_input = config.get('elements', 'username_name')
        return username_input

    @staticmethod
    def get_password_input():
        password_input = config.get('elements', 'password_name')
        return password_input

    @staticmethod
    def get_login_button():
        login_button = config.get('elements', 'login_button_class')
        return login_button

    @staticmethod
    def get_title():
        title = config.get('elements', 'dashboard_title')
        return title
