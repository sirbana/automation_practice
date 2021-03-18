from selenium.webdriver.support.select import Select

from testcase.locators.contact_us_page_locators import ContactUsPageLocators
from testcase.pages.base_page import BasePage


class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ContactUsPageLocators(self.driver)

    def subject_heading_dropdown(self, subject):
        select_element = self.locators.subject_heading_dropdown()
        element = Select(select_element)
        element.select_by_visible_text(subject)

    def email_address_input(self, email):
        element = self.locators.email_address_input()
        element.send_keys(email)

    def order_reference_input(self, reference):
        element = self.locators.order_reference_input()
        element.send_keys(reference)

    def message_input_contact_us(self, message):
        element = self.locators.message_input_contactus()
        element.send_keys(message)

    def click_file_Upload_button(self):
        element = self.locators.file_upload_button()
        element.click()

    def click_send_button(self):
        element = self.locators.send_button()
        element.click()

    def alert_message_succes(self):
        element = self.locators.alert_success_message()
        return element.text

    def alert_message_missing(self):
        element = self.locators.alert_message_no_email()
        return element.text
