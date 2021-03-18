from testcase.locators.category_page_locators import CategoryPageLocators
from testcase.pages.base_page import BasePage


class CategoryProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CategoryPageLocators(self.driver)

    def products_list(self):
        elements = self.locators.products()
        products_list = []
        for elem in elements:
            products_list.append(elem.text)

        return products_list
