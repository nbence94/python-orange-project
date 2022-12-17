from selenium.webdriver.common.by import By
from utilities.read_login import ReadConfig


class LoginPage:

    username_name = ReadConfig.get_username_input()
    password_name = ReadConfig.get_password_input()
    login_button_xpath = ReadConfig.get_login_button()
    title_xpath = ReadConfig.get_title()

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.implicitly_wait(5)
        input_field = self.driver.find_element(By.XPATH, self.username_name)
        input_field.clear()
        input_field.send_keys(username)

    def set_password(self, password):
        self.driver.implicitly_wait(5)
        input_field = self.driver.find_element(By.XPATH, self.password_name)
        input_field.clear()
        input_field.send_keys(password)

    def click_login_button(self):
        self.driver.implicitly_wait(5)
        input_field = self.driver.find_element(By.XPATH, self.login_button_xpath)
        input_field.click()

    def get_title(self):
        self.driver.implicitly_wait(5)
        site_title = self.driver.find_element(By.XPATH, self.title_xpath)
        return site_title.text
