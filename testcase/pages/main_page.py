from selenium import webdriver

from testcase.locators.main_page_locators import MainPageLocators
from testcase.pages.base_page import BasePage, click_non_interactible_element


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators(self.driver)

    def is_title_matches(self):
        return "My Store" in self.driver.title

    def click_sing_in_button(self):
        element = self.locators.sign_in_button()
        element.click()

    def send_keys_in_search(self, product):
        element = self.locators.search_field_input()
        element.send_keys(product)

    def click_search_button(self):
        element = self.locators.search_button()
        element.click()

    def click_dresses_link(self):
        element = self.locators.category_dresses_link()
        element.click()

    def click_contact_us_button(self):
        element = self.locators.contact_us_button()
        element.click()

    def click_cart_button(self):
        element = self.locators.shopping_cart_button()
        element.click()

    def hover_nth_product(self, n):
        element = self.locators.nth_product(n)
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def click_add_to_cart_nth_product_button(self, n):
        element = self.locators.add_to_cart_nth_product_button(n)
        element.click()

    def click_continue_to_checkout_button(self):
        element = self.locators.continue_to_checkout_button()
        element.click()

    def click_button_check_out(self):
        element = self.locators.button_check_out()
        element.click()

    def hover_shopping_cart_button(self):
        element = self.locators.shopping_cart_button()
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def click_continue_shopping_button(self):
        element = self.locators.continue_shopping_button()
        click_non_interactible_element(self.driver, element)

    def title_of_nth_product(self, n):
        element = self.locators.title_of_nth_product(n)
        return element.text
