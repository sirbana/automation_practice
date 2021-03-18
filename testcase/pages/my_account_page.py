from testcase.locators.my_account_page_locators import MyAccountPageLocators
from testcase.pages.base_page import BasePage


class MyAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MyAccountPageLocators(self.driver)

    def registration_message(self):
        element = self.locators.registration_message()
        return element.text