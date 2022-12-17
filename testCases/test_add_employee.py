from pageObjects.LoginPage import LoginPage
from pageObjects.Navigation import NavigationBar
from pageObjects.Employees import Employees
from utilities.read_login import ReadConfig
from utilities.read_navigation import ReadNavigation
from selenium import webdriver
from datetime import datetime


class TestAddEmployee:

    url = ReadConfig.get_url()
    username_value = ReadConfig.get_username()
    password_value = ReadConfig.get_password()

    first_name_value = 'Roger'
    middle_name_value = ''
    last_name_value = 'Stephenson'

    def test_add_employee_normal(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username_value)
        self.lp.set_password(self.password_value)
        self.lp.click_login_button()

        # Navigate to PIM
        self.n = NavigationBar(self.driver)
        self.n.select_menu(ReadNavigation.get_pim())

        # Add new Employee
        self.emp = Employees(self.driver)
        self.emp.click_on_add_employee()
        self.emp.set_first_name(self.first_name_value)
        self.emp.set_last_name(self.last_name_value)
        self.emp.click_on_save()

        # Validate
        if self.middle_name_value == "":
            expected_name = self.first_name_value + " " + self.last_name_value
        else:
            expected_name = self.first_name_value + " " + self.middle_name_value + " " + self.last_name_value

        actual_name = self.emp.get_employee_name()

        print(expected_name + " == " + actual_name)
        if expected_name == actual_name:
            assert True
        else:
            today = datetime.now()
            d1 = today.strftime("%d_%m_%Y_%H_%M_%S")
            self.driver.save_screenshot("..\\Screenshots\\add_employee_problem_" + d1 +".png")
            assert False
