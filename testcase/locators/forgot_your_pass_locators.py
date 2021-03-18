from testcase.locators.base_page_locators import BasePageLocators


class ForgotYourPassLocators(BasePageLocators):
    def forgot_your_pass_message(self):
        return self.driver.find_element_by_css_selector('.box>p')