from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def basket_price(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def product_name_in_basket(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text

    def basket_price_should_be_equal_to_product_price(self):
        assert self.basket_price() == self.product_price(), "Basket price is not equal to product price"

    def product_name_should_be_equal_to_product_name_in_basket(self):
        assert self.product_name() == self.product_name_in_basket(), "Product name is not equal to product name in basket"

    # self — ссылка на текущий объект (browser, url и методы).
    # * перед локатором — распаковка (By.XPATH, "...") для find_element.
    # Локаторы не в этом файле — они в ProductPageLocators, чтобы не смешивать «где искать» и «что делать».

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not presented, but should be"

    def should_be_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET), \
        "Product is not presented in basket"

    def should_not_be_product_in_basket(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_IN_BASKET), \
        "Product is still presented in basket"
