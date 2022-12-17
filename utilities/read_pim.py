import configparser

config = configparser.RawConfigParser()
config.read(r"..\Configuration\pim.ini")


class ReadPim:

    @staticmethod
    def get_add_employee_selector():
        return config.get("location", "add_employee_button_selector")

    @staticmethod
    def get_first_name_selector():
        return config.get("location", "first_name_selector")

    @staticmethod
    def get_middle_name_selector():
        return config.get("location", "middle_name_selector")

    @staticmethod
    def get_last_name_selector():
        return config.get("location", "last_name_selector")

    @staticmethod
    def get_id_selector():
        return config.get("location", "id_selector")

    @staticmethod
    def get_picture_selector():
        return config.get("location", "browse_pic_selector")

    @staticmethod
    def get_save_button_selector():
        return config.get("location", "save_button_selector")

    @staticmethod
    def get_details_employee_name():
        return config.get("location", "details_employee_name_selector")
