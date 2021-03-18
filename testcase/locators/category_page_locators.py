from testcase.locators.base_page_locators import BasePageLocators


class CategoryPageLocators(BasePageLocators):
    def products(self):
        return self.driver.find_elements_by_css_selector('.product-container>div>h5>a.product-name')