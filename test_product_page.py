import pytest
from pages.product_page import ProductPage

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                    pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail(reason="Known bug: wrong product name in basket message"),
                                    ),
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link  ):
    # Шаг 0. Задаём адрес страницы
    #Закомментировал, так как добавил параметризацию link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # Шаг 1. Создаём «инструкцию» для страницы товара
    page = ProductPage(browser, link)
    # Шаг 2. Открываем страницу товара
    page.open()
    # Шаг 3. Добавляем товар в корзину
    page.add_to_basket()
    # Шаг 4. Проверяем, что имя добавленного товара совпадает с сообщением о добавлении товара в корзину
    page.product_name_should_be_equal_to_product_name_in_basket()
    # Шаг 5. Проверяем, что цена добавленного товара совпадает с ценой товара в корзине
    page.basket_price_should_be_equal_to_product_price()

    # Вся цепочка одной фразой
    # Открыл браузер
    #   → зашёл на страницу книги
    #     → нажал «Добавить в корзину»
    #       → решил alert-задачку
    #         → проверил: цена в корзине = цена товара
@pytest.mark.xfail(reason="Success message is present after adding to basket")
def test_guest_cant_see_not_success_message_after_adding_product_to_basket(browser):
    # Шаг 1. Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    # Шаг 2. Добавляем товар в корзину
    page.add_to_basket()
    # Шаг 3. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    # Шаг 1. Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    # Шаг 2. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Success message does not disappear from DOM")
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Шаг 1. Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    # Шаг 2. Добавляем товар в корзину
    page.add_to_basket()
    # Шаг 3. Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.message_disappeared_after_adding_product_to_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Шаг 1. Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # Шаг 2. Переходит в корзину по кнопке в шапке
    basket_page = page.open_basket_page()
    # Шаг 3. Ожидаем, что в корзине нет товаров
    basket_page.should_not_be_products_in_basket()
    # Шаг 4. Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_empty_basket_message()