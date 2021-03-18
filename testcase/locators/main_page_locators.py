from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from testcase.locators.base_page_locators import BasePageLocators


class MainPageLocators(BasePageLocators):
    def sign_in_button(self):
        return self.driver.find_element_by_css_selector(".header_user_info>a.login")

    def search_field_input(self):
        return self.driver.find_element_by_id('search_query_top')

    def search_button(self):
        return self.driver.find_element_by_css_selector('#searchbox>button.button-search')

    def category_dresses_link(self):
        return self.driver.find_element_by_css_selector('ul.sf-menu>li>a[title="Dresses"]')

    def contact_us_button(self):
        return self.driver.find_element_by_css_selector('#contact-link>a')

    def shopping_cart_button(self):
        return self.driver.find_element_by_css_selector('.shopping_cart>a')

    def nth_product(self, n):
        return self.driver.find_element_by_css_selector(
            ".tab-content>ul:first-child>li:nth-child(" + str(n) + ")>div>div>div.product-image-container>a:first-child"
        )

    def add_to_cart_nth_product_button(self, n):
        return self.driver.find_element_by_css_selector(
            "ul#homefeatured>li:nth-child(" + str(n) + ")>div.product-container>div>.button-container>a.ajax_add_to_cart_button"
        )

    def title_of_nth_product(self, n):
        return self.driver.find_element_by_css_selector(
            "ul#homefeatured>li:nth-child(" + str(n) + ")>div.product-container>div.right-block>h5"
        )

    def second_product_add_to_cart_button(self):
        return self.driver.find_element_by_css_selector

    def continue_to_checkout_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.layer_cart_cart>.button-container>a'))
        )

    def button_check_out(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, 'button_order_cart'))
        )

    def shopping_cart_button(self):
        return self.driver.find_element_by_css_selector('.shopping_cart>a')

    def continue_shopping_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.continue'))
        )