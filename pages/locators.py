from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_PAGE_URL = "/login"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "registration_form")
    LOGIN_FIELD_EMAIL = (By.ID, "id_login-username")
    LOGIN_FIELD_PASSWORD = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.XPATH, "//button[@name='login_submit']")
    REGISTER_FIELD_EMAIL = (By.XPATH, "//input[@id='id_registration-email']")
    REGISTER_FIELD_PASSWORD1 = (By.XPATH, "//input[@id='id_registration-password1']")
    REGISTER_FIELD_PASSWORD2 = (By.XPATH, "//input[@id='id_registration-password2']")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_NAME = (By.XPATH, "//h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    BASKET_PRICE = (By.XPATH, "//div[contains(@class, 'alert-info')]//strong")
    PRODUCT_NAME_IN_BASKET = (By.XPATH,
                              "//div[contains(@class, 'alertinner')][contains(., 'has been added to your basket')]//strong")
    SUCCESS_MESSAGE = (By.XPATH,
                       "//div[contains(@class, 'alertinner')][contains(normalize-space(.), 'has been')]")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini .btn-group > a")

class BasketPageLocators():
    PRODUCTS_IN_BASKET = (By.XPATH, "//form[@id='basket_formset']")
    NO_PRODUCTS_IN_BASKET = (
        By.XPATH,
        "//div[@id='content_inner']//p[contains(normalize-space(.), 'Your basket is empty')]",
    )