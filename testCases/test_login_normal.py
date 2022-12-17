from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utilities.read_login import ReadConfig
from selenium import webdriver

class TestLogin:

    username_value = ReadConfig.get_username()
    password_value = ReadConfig.get_password()
    url = ReadConfig.get_url()

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)

        self.lp.set_username(self.username_value)
        self.lp.set_password(self.password_value)

        self.lp.click_login_button()

        # Check the login
        title = self.lp.get_title()
        if title == "Dashboard":
            assert True
        else:
            assert False

