from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверяю, что в урле есть подстрока login
        assert LoginPageLocators.LOGIN_PAGE_URL in self.browser.current_url, \
            f"Неверный URL: {self.browser.current_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        # Вводим E-mail
        self.browser.find_element(*LoginPageLocators.REGISTER_FIELD_EMAIL).send_keys(email)
        # Вводим пароль и подтверждение пароля
        self.browser.find_element(*LoginPageLocators.REGISTER_FIELD_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FIELD_PASSWORD2).send_keys(password)
        # Нажимаем на кнопку "Зарегистрироваться"
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        # Проверяем сообщение об успешной регистрации
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_SUCCESS_MESSAGE), "Success message is not presented"