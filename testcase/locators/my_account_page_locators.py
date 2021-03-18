from testcase.locators.base_page_locators import BasePageLocators


class MyAccountPageLocators(BasePageLocators):
    def registration_message(self):
        return self.driver.find_element_by_css_selector('#center_column>.info-account')