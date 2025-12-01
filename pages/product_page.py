import math
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        # Проверяем, есть ли alert (только для промо-страниц)
        try:
            self.solve_quiz_and_get_code()
        except NoAlertPresentException:
            # Если alert нет - это нормально (не промо-страница)
            pass

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_product_added_to_basket(self):
        product_name = self.get_product_name()
        product_price = self.get_product_price()
        self.should_be_success_message()
        self.should_be_correct_product_name(product_name)
        self.should_be_basket_total()
        self.should_be_correct_basket_total(product_price)

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented"

    def should_be_correct_product_name(self, expected_name):
        actual_name = self.browser.find_element(*ProductPageLocators.SUCCESS_PRODUCT_NAME).text
        assert actual_name == expected_name, \
            f"Product name in message '{actual_name}' doesn't match '{expected_name}'"

    def should_be_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), \
            "Basket total message is not presented"

    def should_be_correct_basket_total(self, expected_price):
        actual_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert actual_price == expected_price, \
            f"Basket total '{actual_price}' doesn't match '{expected_price}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but it didn't"