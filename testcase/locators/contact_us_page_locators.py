from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from testcase.locators.base_page_locators import BasePageLocators


class ContactUsPageLocators(BasePageLocators):
    def subject_heading_dropdown(self):
        return self.driver.find_element_by_id('id_contact')

    def email_address_input(self):
        return self.driver.find_element_by_id('email')

    def order_reference_input(self):
        return self.driver.find_element_by_id('id_order')

    def message_input_contactus(self):
        return self.driver.find_element_by_id('message')

    def file_upload_button(self):
        return self.driver.find_element_by_id('fileUpload')

    def send_button(self):
        return self.driver.find_element_by_id('submitMessage')

    def alert_success_message(self):
        return self.driver.find_element_by_css_selector('.center_column>.alert-success')

    def alert_message_no_email(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.alert-danger>ol>li'))
        )