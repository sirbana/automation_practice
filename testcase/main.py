import unittest
import time
from selenium import webdriver

import testcase.pages.cart_page
import testcase.pages.category_products_page
import testcase.pages.contact_us_page
import testcase.pages.forgot_your_pass_page
import testcase.pages.main_page
import testcase.pages.my_account_page
import testcase.pages.registration_page
import testcase.pages.search_result_page
import testcase.pages.sign_in_page


class AutomationPracticeComTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\chromedriver.exe")
        self.driver.get("http://automationpractice.com/index.php")

    def tearDown(self):
        self.driver.close()

    def test_title(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        assert main_page.is_title_matches()

    def test_registration_invalid(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        main_page.click_sing_in_button()

        sign_in_page = testcase.pages.sign_in_page.SignInPage(self.driver)
        sign_in_page.input_email_in_register("anan")

        sign_in_page.click_register_button()
        message = sign_in_page.register_error_message()
        assert message == 'Invalid email address.'

    def test_registration_valid(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        main_page.click_sing_in_button()

        sign_in_page = testcase.pages.sign_in_page.SignInPage(self.driver)
        sign_in_page.input_email_in_register('abd@harakirimail.com')

        sign_in_page.click_register_button()

        register_page = testcase.pages.registration_page.RegistrationPage(self.driver)
        assert register_page.page_heading().lower() == 'your personal information'

    def test_valid_search(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        main_page.send_keys_in_search('t-shirt')
        main_page.click_search_button()

        search_result_page = testcase.pages.search_result_page.SearchResultPage(self.driver)
        assert 't-shirt' in search_result_page.first_result_title().lower()

    def test_invalid_search(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        main_page.send_keys_in_search("cucu")
        main_page.click_search_button()

        search_result_page = testcase.pages.search_result_page.SearchResultPage(self.driver)
        assert search_result_page.invalid_search_message() == 'No results were found for your search "cucu"'

    def test_same_category_products(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        main_page.click_dresses_link()

        category_page = testcase.pages.category_products_page.CategoryProductsPage(self.driver)
        for product in category_page.products_list():
            assert 'dress' in product.lower()

    def test_valid_registration(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        main_page.click_sing_in_button()

        sign_in_page = testcase.pages.sign_in_page.SignInPage(self.driver)
        sign_in_page.input_email_in_register("aha2532@harakirimail.com")
        sign_in_page.click_register_button()

        register_page = testcase.pages.registration_page.RegistrationPage(self.driver)
        assert register_page.page_heading().lower() == 'your personal information'

        register_page.gender_selection()
        register_page.firstname_input('Iulia')

        register_page.lastname_input('buhuhi')
        register_page.pass_input('abcdeklr')

        register_page.select_days_dropdown('1')
        register_page.select_months_dropdown('3')
        register_page.select_years_dropdown('2014')

        assert register_page.input_your_address_firstname() == 'Iulia'
        assert register_page.input_your_address_lastname() == 'buhuhi'

        register_page.input_your_address_company('polus')
        register_page.input_your_address_address('strada Colinei, bl34, ap3')
        register_page.input_your_address_city('Baia')

        register_page.select_state_dropdown('Oregon')
        register_page.input_your_address_postcode('50040')
        register_page.select_country_dropdown('United States')
        register_page.input_your_address_phone('567 899 9999')
        register_page.input_your_address_phone_mobile('989 989 0909')
        register_page.input_your_address_alias('Home')

        register_page.click_submit_button()
        my_account_page = testcase.pages.my_account_page.MyAccountPage(self.driver)
        assert my_account_page.registration_message() == 'Welcome to your account. Here you can manage all of your personal information and orders.'

    def test_valid_login(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        main_page.click_sing_in_button()

        sign_in_page = testcase.pages.sign_in_page.SignInPage(self.driver)
        sign_in_page.input_email_in_signin('aha2532@harakirimail.com')
        sign_in_page.input_pass_in_signin('abcdeklr')
        sign_in_page.click_login_button()
        my_account_page = testcase.pages.my_account_page.MyAccountPage(self.driver)
        assert my_account_page.registration_message() == 'Welcome to your account. Here you can manage all of your personal information and orders.'

    def test_sign_in_without_email_and_pass(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        main_page.click_sing_in_button()
        sign_in_page = testcase.pages.sign_in_page.SignInPage(self.driver)
        sign_in_page.input_email_in_signin('')
        sign_in_page.input_pass_in_signin('')
        sign_in_page.click_login_button()
        assert sign_in_page.alert_email_missing_message() == 'An email address required.'

    def test_sign_in_without_pass(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        main_page.click_sing_in_button()
        sign_in_page = testcase.pages.sign_in_page.SignInPage(self.driver)
        sign_in_page.input_email_in_signin('aha2532@harakirimail.com')
        sign_in_page.input_pass_in_signin('')
        sign_in_page.click_login_button()
        assert sign_in_page.alert_email_missing_message() == 'Password is required.'

    def test_forgot_your_pass_valid(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        main_page.click_sing_in_button()
        sign_in_page = testcase.pages.sign_in_page.SignInPage(self.driver)
        sign_in_page.forgot_password_link()
        forgot_your_pass = testcase.pages.forgot_your_pass_page.ForgotYourPassPage(self.driver)
        assert forgot_your_pass.forgot_your_pass_message() == 'Please enter the email address you used to register. We will then send you a new password.'

    # def test_sign_in_invalid_email_address(self):
    def test_contact_us_valid(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        main_page.click_contact_us_button()
        contact_us_page = testcase.pages.contact_us_page.ContactUsPage(self.driver)
        contact_us_page.subject_heading_dropdown('Customer service')
        contact_us_page.email_address_input('aha@harakirimail.com')
        contact_us_page.order_reference_input('reference 01')
        contact_us_page.message_input_contact_us('Buna ziua, \nvreau sa ma fac o cerere de retur\n hop si asa.')
        contact_us_page.click_send_button()
        assert contact_us_page.alert_message_succes() == 'Your message has been successfully sent to our team.'
        time.sleep(5)

    def test_contact_us_no_credentials(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        main_page.click_contact_us_button()
        contact_us_page = testcase.pages.contact_us_page.ContactUsPage(self.driver)

        contact_us_page.click_send_button()
        assert contact_us_page.alert_message_missing() == 'Invalid email address.'

    def test_contact_us_without_message(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        main_page.click_contact_us_button()
        contact_us_page = testcase.pages.contact_us_page.ContactUsPage(self.driver)
        contact_us_page.email_address_input('aha@harakirimail.com')
        contact_us_page.click_send_button()
        assert contact_us_page.alert_message_missing() == 'The message cannot be blank.'

    def test_contact_us_only_with_email_and_message(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        main_page.click_contact_us_button()
        contact_us_page = testcase.pages.contact_us_page.ContactUsPage(self.driver)
        contact_us_page.email_address_input('aha@harakirimail.com')
        contact_us_page.message_input_contact_us('Buna ziua, \nvreau sa ma fac o cerere de retur\n hop si asa.')
        contact_us_page.click_send_button()
        assert contact_us_page.alert_message_missing() == 'Please select a subject from the list provided.'

    def test_contact_us_with_email_subject_and_message(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        main_page.click_contact_us_button()
        contact_us_page = testcase.pages.contact_us_page.ContactUsPage(self.driver)
        contact_us_page.subject_heading_dropdown('Customer service')
        contact_us_page.email_address_input('aha@harakirimail.com')
        contact_us_page.message_input_contact_us('Buna ziua, \nvreau sa ma fac o cerere de retur\n hop si asa.')
        contact_us_page.click_send_button()
        assert contact_us_page.alert_message_succes() == 'Your message has been successfully sent to our team.'

    def test_contact_us_very_long_message(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        main_page.click_contact_us_button()
        contact_us_page = testcase.pages.contact_us_page.ContactUsPage(self.driver)
        contact_us_page.subject_heading_dropdown('Customer service')
        contact_us_page.email_address_input('aha@harakirimail.com')
        contact_us_page.message_input_contact_us('Buna ziua, \nvreau sa ma fac o cerere de retur\n hop si asa.' * 1000)
        contact_us_page.click_send_button()
        assert contact_us_page.alert_message_succes() == 'Your message has been successfully sent to our team.'

    def test_add_to_cart(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        # main_page.click_cart_button()

        main_page.hover_nth_product(1)
        main_page.click_add_to_cart_nth_product_button(1)
        main_page.click_continue_to_checkout_button()
        cart_page = testcase.pages.cart_page.CartPage(self.driver)

        assert '1 ' in cart_page.heading_counter_number_of_items()

    def test_add_multiple_products_to_cart(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)

        for i in range(1, 6):
            main_page.hover_nth_product(i)
            main_page.click_add_to_cart_nth_product_button(i)
            main_page.click_continue_shopping_button()
        main_page.hover_shopping_cart_button()
        main_page.click_button_check_out()

        cart_page = testcase.pages.cart_page.CartPage(self.driver)

        assert '5' in cart_page.heading_counter_number_of_items()

    def test_same_product_in_cart_as_added(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)
        product_names = []
        for i in range(1, 5):
            main_page.hover_nth_product(i)
            main_page.click_add_to_cart_nth_product_button(i)
            main_page.click_continue_shopping_button()
            product_names.append(main_page.title_of_nth_product(i))

        main_page.hover_shopping_cart_button()
        main_page.click_button_check_out()

        cart_page = testcase.pages.cart_page.CartPage(self.driver)
        cart_product_names = cart_page.cart_product_names()
        assert cart_product_names == product_names

        time.sleep(5)

    def test_empty_cart(self):
        main_page = testcase.pages.main_page.MainPage(self.driver)

        for i in range(1, 2):
            main_page.hover_nth_product(i)
            main_page.click_add_to_cart_nth_product_button(i)
            main_page.click_continue_shopping_button()
        main_page.hover_shopping_cart_button()
        main_page.click_button_check_out()

        cart_page = testcase.pages.cart_page.CartPage(self.driver)
        for i in range(1, 2):
            cart_page.click_of_nth_recycle_bin(1)

        assert 'o' in cart_page.heading_counter_number_of_items()
        assert cart_page.message_no_product_in_cart() == 'Your shopping cart is empty.'


if __name__ == '__main__':
    unittest.main()
