from configparser import RawConfigParser

config = RawConfigParser()
config.read(r'..\Configuration\navigation.ini')


class ReadNavigation:

    @staticmethod
    def get_main_button():
        return config.get('location', 'open_close')

    @staticmethod
    def get_elements():
        return config.get('location', 'menu_xpath')

    @staticmethod
    def get_admin():
        return config.get('elements', 'admin')

    @staticmethod
    def get_pim():
        return config.get('elements', 'employees')
