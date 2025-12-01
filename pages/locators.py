from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    # Кнопка добавления в корзину
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    # Название товара
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")

    # Цена товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    # Сообщения об успехе
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    SUCCESS_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success strong")

    # Сообщение со стоимостью корзины
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info strong")

    class ProductPageLocators():
        ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
        PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
        PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
        SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
        SUCCESS_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success strong")
        BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info")
        BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info strong")
        LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")