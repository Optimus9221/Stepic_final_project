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

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    pass

def test_guest_cant_see_success_message(browser):
    pass

def test_message_disappeared_after_adding_product_to_basket(browser):
    pass