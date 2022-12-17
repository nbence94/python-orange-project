from selenium.webdriver.common.by import By
from utilities.read_navigation import ReadNavigation


class NavigationBar:

    oc_button_xpath = ReadNavigation.get_main_button()
    menu_selection_xpath = ReadNavigation.get_elements()

    def __init__(self, driver):
        self.driver = driver

    def click_open_close(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.oc_button_xpath).click()

    def select_menu(self, menu):
        self.driver.implicitly_wait(5)
        selection = self.driver.find_elements(By.XPATH, self.menu_selection_xpath)

        for e in selection:
            if e.text.lower() == menu.lower():
                e.click()
                break
