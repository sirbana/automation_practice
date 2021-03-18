from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePageLocators(object):
    def __init__(self, driver):
        self.driver = driver


def wait_for_element_to_be_visible(driver, by, selector):
    return WebDriverWait(driver, 5).until(EC.visibility_of_element_located((by, selector)))