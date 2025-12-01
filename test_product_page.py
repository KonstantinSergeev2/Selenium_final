from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    # Ссылка с промоакцией
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    # Инициализируем Page Object
    page = ProductPage(browser, link)

    # Открываем страницу товара
    page.open()

    # Добавляем товар в корзину
    page.add_to_basket()

    # Проверяем, что товар добавлен
    page.should_be_success_message()
    page.should_be_correct_product_name()
    page.should_be_basket_total()
    page.should_be_correct_basket_total()