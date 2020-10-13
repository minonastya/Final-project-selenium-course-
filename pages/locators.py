from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    SIGN_IN_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    SIGN_IN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    SIGN_UP_LOGIN = (By.CSS_SELECTOR, "#register_form")
    SIGN_UP_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password")
    SIGN_IN_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")