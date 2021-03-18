from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from testcase.locators.base_page_locators import BasePageLocators


class SearchPageLocators(BasePageLocators):
    def first_result_product(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR,
                ".right-block>h5:first-child>a"
            ))
        )

    def invalid_search_message(self):
        return self.driver.find_element_by_css_selector('.alert-warning')