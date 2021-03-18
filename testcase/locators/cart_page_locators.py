from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from testcase.locators.base_page_locators import BasePageLocators


class CartPageLocators(BasePageLocators):
    def heading_counter_number_of_items(self):
        return self.driver.find_element_by_css_selector('.heading-counter')

    def titles_of_items_in_cart(self):
        return self.driver.find_elements_by_css_selector('.cart_description>.product-name>a')

    def nth_recycle_bin(self, n):

        return self.driver.find_element_by_css_selector(
            "tbody>.cart_item:nth-child(" + str(n) + ")>.cart_delete>div>a"
        )

    def alert_no_product_in_cart(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.alert-warning'))
        )