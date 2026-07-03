from pages.base_page import BasePage
from .locators import MainPageLocators, BasePageLocators
from .login_page import LoginPage
from pages.basket_page import BasketPage

class MainPage(BasePage):
    def open_basket_page(self):
        basket_button = self.browser.find_element(*MainPageLocators.VIEW_BASKET_BUTTON)
        basket_button.click()
        return BasketPage(browser=self.browser, url=self.browser.current_url)

