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