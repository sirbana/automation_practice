from testcase.locators.sign_in_locators import SignInPageLocators
from testcase.pages.base_page import BasePage


class SignInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SignInPageLocators(self.driver)

    def input_email_in_register(self, email):
        element = self.locators.email_register_input()
        element.send_keys(email)

    def click_register_button(self):
        element = self.locators.register_button()
        element.click()

    def register_error_message(self):
        element = self.locators.register_error_message()
        return element.text

    def input_email_in_signin(self, email):
        element = self.locators.sign_in_email_input()
        element.send_keys(email)

    def input_pass_in_signin(self, password):
        element = self.locators.sign_in_pass_input()
        element.send_keys(password)

    def click_login_button(self):
        element = self.locators.sign_in_button()
        element.click()

    def alert_email_missing_message(self):
        element = self.locators.alert_message()
        return element.text

    def forgot_password_link(self):
        element = self.locators.forgot_your_pass()
        element.click()