from .base_page import BasePage
from .locators import LoginPageLocators
from pages import data

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Is not login url"

    def sign_up(self, login, password, repeat_password):
        user_login = self.browser.find_element(*LoginPageLocators.SIGN_UP_LOGIN)
        user_password = self.browser.find_element(*LoginPageLocators.SIGN_UP_PASSWORD)
        user_repeat_password = self.browser.find_element(*LoginPageLocators.SIGN_UP_REPEAT_PASSWORD)
        button_sign_up = self.browser.find_element(*LoginPageLocators.SIGN_UP_BUTTON)
        user_login.send_keys(login)
        user_password.send_keys(password)
        user_repeat_password.send_keys(repeat_password)
        button_sign_up.click()

    def success_registration(self):
        assert data.MAIN_PAGE_LINK in self.browser.current_url, "Registration finished with an error"

    def sign_in(self, login, password):
        user_login = self.browser.find_element(*LoginPageLocators.SIGN_IN_LOGIN)
        user_password = self.browser.find_element(*LoginPageLocators.SIGN_IN_PASSWORD)
        button_sign_up = self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON)
        user_login.send_keys(login)
        user_password.send_keys(password)
        button_sign_up.click()

    def success_login(self):
        assert data.MAIN_PAGE_LINK in self.browser.current_url, "Login finished with an error"



