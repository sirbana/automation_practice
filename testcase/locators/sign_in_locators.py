from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from testcase.locators.base_page_locators import BasePageLocators


class SignInPageLocators(BasePageLocators):
    def email_register_input(self):
        return self.driver.find_element_by_id("email_create")

    def register_button(self):
        return self.driver.find_element_by_id("SubmitCreate")

    def register_error_message(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "create_account_error"))
        )

    def creation_form(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "account-creation_form"))
        )

    def sign_in_email_input(self):
        return self.driver.find_element_by_id('email')

    def sign_in_pass_input(self):
        return self.driver.find_element_by_id('passwd')

    def sign_in_button(self):
        return self.driver.find_element_by_id('SubmitLogin')

    def alert_message(self):
        return self.driver.find_element_by_css_selector('.alert-danger>ol>li')

    def forgot_your_pass(self):
        return self.driver.find_element_by_css_selector('.lost_password>a')