class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


def click_non_interactible_element(driver, element):
    """ Selenium doesn't support clicking non-interactible elements (eg: span).
    So we need to run a javascript, that simulates the click. """
    driver.execute_script("arguments[0].click();", element)