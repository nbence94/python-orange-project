from pageObjects.LoginPage import LoginPage
from pageObjects.Navigation import NavigationBar
from utilities.read_login import ReadConfig
from utilities.read_navigation import ReadNavigation
from selenium import webdriver
import time

class TestAddEmployee:

    url = ReadConfig.get_url()
    username_value = ReadConfig.get_username()
    password_value = ReadConfig.get_password()

    def test_add_employee_normal(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username_value)
        self.lp.set_password(self.password_value)
        self.lp.click_login_button()

        #Navigate
        self.n = NavigationBar(self.driver)
        self.n.select_menu(ReadNavigation.get_pim())
        time.sleep(10)
