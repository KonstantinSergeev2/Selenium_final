from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    # Попробуйте разные варианты селекторов для ссылки на корзину:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")  # вариант 1
    # BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a")  # вариант 2
    # BASKET_LINK = (By.XPATH, "//a[contains(text(), 'View basket')]")  # вариант 3

class MainPageLocators():
    # Теперь пустой, так как все перенесли в BasePageLocators
    pass


class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    SUCCESS_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info strong")


class BasketPageLocators():
    # Товары в корзине
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

    # Сообщение о пустой корзине
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    # Или так: EMPTY_BASKET_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your basket is empty')]")