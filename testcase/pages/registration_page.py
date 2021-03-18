from selenium.webdriver.support.select import Select

from testcase.locators.registration_page_locators import RegistrationPageLocators
from testcase.pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RegistrationPageLocators(self.driver)

    def page_heading(self):
        element = self.locators.registration_heading()
        return element.text

    def firstname_input(self, firstname):
        elements = self.locators.first_name_input()
        elements.send_keys(firstname)

    def gender_selection(self):
        elements = self.locators.gender_selector()
        elements.click()

    def lastname_input(self, lastname):
        elements = self.locators.lastname_locator()
        elements.send_keys(lastname)

    def pass_input(self, password):
        elements = self.locators.pass_input()
        elements.send_keys(password)

    def select_days_dropdown(self, day):
        select_element = self.locators.dropdown_date_days()
        element = Select(select_element)
        element.select_by_value(day)

    def select_months_dropdown(self, month):
        select_element = self.locators.dropdown_date_months()
        element = Select(select_element)
        element.select_by_value(month)

    def select_years_dropdown(self, year):
        select_element = self.locators.dropdown_date_years()
        element = Select(select_element)
        element.select_by_value(year)

    def input_your_address_firstname(self):
        element = self.locators.your_address_firstname_input()
        element.click()
        return element.get_attribute("value")

    def input_your_address_lastname(self):
        elements = self.locators.your_address_lastname_input()
        elements.click()
        return elements.get_attribute('value')

    def input_your_address_company(self, company):
        elements = self.locators.your_address_company()
        elements.send_keys(company)

    def input_your_address_address(self, address):
        elements = self.locators.your_address_address()
        elements.send_keys(address)

    def input_your_address_city(self, city):
        elements = self.locators.your_address_city()
        elements.send_keys(city)

    def select_state_dropdown(self, state):
        state_element = self.locators.your_address_state()
        element = Select(state_element)
        element.select_by_visible_text(state)

    def input_your_address_postcode(self, postcode):
        element = self.locators.your_address_postcode()
        element.send_keys(postcode)

    def select_country_dropdown(self, country):
        state_element = self.locators.your_address_country()
        element = Select(state_element)
        element.select_by_visible_text(country)

    def input_your_address_phone(self, phone):
        element = self.locators.your_address_phone()
        element.send_keys(phone)

    def input_your_address_phone_mobile(self, mobile):
        element = self.locators.your_address_phone_mobile(mobile)
        element.send_keys(mobile)

    def input_your_address_alias(self, alias):
        element = self.locators.your_address_alias()
        element.clear()
        element.send_keys(alias)

    def click_submit_button(self):
        element = self.locators.registration_button()
        element.click()