import pytest
from pages.product_page import ProductPage


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    1. Открываем страницу товара (БЕЗ промо)
    2. Добавляем товар в корзину
    3. Проверяем, что нет сообщения об успехе
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    # Добавляем товар в корзину (без alert)
    page.add_to_basket()

    # Проверяем, что нет сообщения об успехе
    # Этот тест ДОЛЖЕН ПАДАТЬ, так как сообщение появляется
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """
    1. Открываем страницу товара
    2. Проверяем, что нет сообщения об успехе
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    # Проверяем, что нет сообщения об успехе
    # Этот тест ДОЛЖЕН ПРОХОДИТЬ, так как мы не добавляли товар
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    1. Открываем страницу товара
    2. Добавляем товар в корзину
    3. Проверяем, что сообщение исчезает
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    # Добавляем товар в корзину (без alert)
    page.add_to_basket()

    # Проверяем, что сообщение исчезает
    # Этот тест ДОЛЖЕН ПАДАТЬ, так как сообщение НЕ исчезает
    page.should_disappear_success_message()