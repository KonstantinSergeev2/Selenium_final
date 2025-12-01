from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException

        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False

    def should_be_basket_page(self):
        # Проверяем, что это страница корзины
        assert "basket" in self.browser.current_url, "Not a basket page"

    def should_be_empty_basket(self):
        # Проверяем, что корзина пуста
        self.should_not_be_products_in_basket()
        self.should_be_empty_basket_message()

    def should_not_be_products_in_basket(self):
        # Проверяем, что нет товаров в корзине
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty, but should be"

    def should_be_empty_basket_message(self):
        # Проверяем, что есть сообщение о пустой корзине
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not presented"