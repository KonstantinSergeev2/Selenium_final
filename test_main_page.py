from pages.main_page import MainPage
from pages.login_page import LoginPage  # Добавляем импорт


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()

    # Переходим на страницу логина
    page.go_to_login_page()

    # Явно инициализируем LoginPage
    login_page = LoginPage(browser, browser.current_url)

    # Проверяем, что это действительно страница логина
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Гость открывает главную страницу
    Переходит в корзину по кнопке в шапке сайта
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста
    """
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()

    # Переходим в корзину
    basket_page = page.go_to_basket_page()

    # Проверяем, что корзина пуста
    basket_page.should_be_empty_basket()