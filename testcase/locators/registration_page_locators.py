from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from testcase.locators.base_page_locators import BasePageLocators


class RegistrationPageLocators(BasePageLocators):
    def registration_heading(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR,
                '#account-creation_form>.account_creation:first-child>h3.page-subheading'
            ))
        )

    def first_name_input(self):
        return self.driver.find_element_by_css_selector('#customer_firstname')

    def gender_selector(self):
        return self.driver.find_element_by_css_selector('#id_gender2')

    def lastname_locator(self):
        return self.driver.find_element_by_css_selector('#customer_lastname')

    def pass_input(self):
        return self.driver.find_element_by_id('passwd')

    def dropdown_date_days(self):
        return self.driver.find_element_by_id('days')

    def dropdown_date_months(self):
        return self.driver.find_element_by_id('months')

    def dropdown_date_years(self):
        return self.driver.find_element_by_id('years')

    def your_address_firstname_input(self):
        return self.driver.find_element_by_id('firstname')

    def your_address_lastname_input(self):
        return self.driver.find_element_by_id('lastname')

    def your_address_company(self):
        return self.driver.find_element_by_id('company')

    def your_address_address(self):
        return self.driver.find_element_by_id('address1')

    def your_address_city(self):
        return self.driver.find_element_by_id('city')

    def your_address_state(self):
        return self.driver.find_element_by_id('id_state')

    def your_address_postcode(self):
        return self.driver.find_element_by_id('postcode')

    def your_address_country(self):
        return self.driver.find_element_by_id('id_country')

    def your_address_phone(self):
        return self.driver.find_element_by_id('phone')

    def your_address_phone_mobile(self, mobile):
        return self.driver.find_element_by_id('phone_mobile')

    def your_address_alias(self):
        return self.driver.find_element_by_id('alias')

    def registration_button(self):
        return self.driver.find_element_by_id('submitAccount')