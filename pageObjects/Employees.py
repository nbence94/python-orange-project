from selenium.webdriver.common.by import By
from utilities.read_pim import ReadPim
import time

class Employees:

    add_employee_button = ReadPim.get_add_employee_selector()
    first_name = ReadPim.get_first_name_selector()
    middle_name = ReadPim.get_middle_name_selector()
    last_name = ReadPim.get_last_name_selector()

    save_button = ReadPim.get_save_button_selector()
    employee_name = ReadPim.get_details_employee_name()

    def __init__(self, driver):
        self.driver = driver

    def click_on_add_employee(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.add_employee_button).click()

    def click_on_save(self):
        self.driver.find_element(By.XPATH, self.save_button).click()

    def get_employee_name(self):
        time.sleep(5)
        self.driver.implicitly_wait(20)
        return self.driver.find_element(By.XPATH, self.employee_name).text

    def set_first_name(self, first_name):
        self.driver.implicitly_wait(5)
        input_field = self.driver.find_element(By.XPATH, self.first_name)
        input_field.clear()
        input_field.send_keys(first_name)

    def set_middle_name(self, middle_name):
        self.driver.implicitly_wait(5)
        input_field = self.driver.find_element(By.XPATH, self.middle_name)
        input_field.clear()
        input_field.send_keys(middle_name)

    def set_last_name(self, last_name):
        self.driver.implicitly_wait(5)
        input_field = self.driver.find_element(By.XPATH, self.last_name)
        input_field.clear()
        input_field.send_keys(last_name)

