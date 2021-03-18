from testcase.locators.search_page_locators import SearchPageLocators
from testcase.pages.base_page import BasePage


class SearchResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SearchPageLocators(self.driver)

    def first_result_title(self):
        element = self.locators.first_result_product()
        return element.text

    def invalid_search_message(self):
        element = self.locators.invalid_search_message()
        return element.text