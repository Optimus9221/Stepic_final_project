import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()      # проверяем ссылку на открывшейся странице

@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Шаг 1. Гость открывает главную страницу
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    # Шаг 2. Переходит в корзину по кнопке в шапке сайта
    basket_page = page.open_basket_page()
    # Шаг 3. Ожидаем, что в корзине нет товаров
    basket_page.should_not_be_products_in_basket()
    # Шаг 4. Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_empty_basket_message()
