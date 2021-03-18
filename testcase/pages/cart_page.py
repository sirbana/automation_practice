from testcase.locators.cart_page_locators import CartPageLocators
from testcase.pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartPageLocators(self.driver)

    def heading_counter_number_of_items(self):
        element = self.locators.heading_counter_number_of_items()
        return element.text

    def cart_product_names(self):
        elements = self.locators.titles_of_items_in_cart()
        list_of_titles = []
        for elem in elements:
            list_of_titles.append(elem.text)
        return list_of_titles

    def click_of_nth_recycle_bin(self, n):
        element = self.locators.nth_recycle_bin(n)
        element.click()

    def message_no_product_in_cart(self):
        element = self.locators.alert_no_product_in_cart()
        return element.text