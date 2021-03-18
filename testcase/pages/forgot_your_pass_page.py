from testcase.locators.forgot_your_pass_locators import ForgotYourPassLocators
from testcase.pages.base_page import BasePage


class ForgotYourPassPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ForgotYourPassLocators(self.driver)

    def forgot_your_pass_message(self):
        element = self.locators.forgot_your_pass_message()
        return element.text