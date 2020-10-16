from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    PROFILE_LINK = (By.CSS_SELECTOR, ".icon-user")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#id_q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.btn-default ")
    IMAGE_OF_PRODUCT = (By.CSS_SELECTOR, ".thumbnail")

class LoginPageLocators():
    SIGN_IN_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    SIGN_IN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "[name = login_submit]")
    SIGN_UP_LOGIN = (By.CSS_SELECTOR, "#id_registration-email")
    SIGN_UP_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    SIGN_UP_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "[name = registration_submit]")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")

class AccountPageLocators():
    ADDRESS_BOOK_TAB = (By.CSS_SELECTOR, "[href *= '/accounts/addresses/']")
    ADD_NEW_ADDRESS = (By.CSS_SELECTOR, "[href *= '/accounts/addresses/add/']")
    APPEAL = (By.CSS_SELECTOR, "#id_title")
    FIRST_NAME = (By.CSS_SELECTOR, "#id_first_name")
    LAST_NAME = (By.CSS_SELECTOR, "#id_last_name")
    FIRST_LINE_ADDRESS = (By.CSS_SELECTOR, "#id_line1")
    SECOND_LINE_ADDRESS = (By.CSS_SELECTOR, "#id_line2")
    THIRD_LINE_ADDRESS = (By.CSS_SELECTOR, "#id_line3")
    CITY = (By.CSS_SELECTOR, "#id_line4")
    STATE = (By.CSS_SELECTOR, "#id_state")
    POSTCODE = (By.CSS_SELECTOR, "#id_postcode")
    COUNTRY = (By.CSS_SELECTOR, "#id_country")
    PHONE = (By.CSS_SELECTOR, "#id_phone_number")
    NOTES = (By.CSS_SELECTOR, "#id_notes")
    SAVE_ADDRESS = (By.CSS_SELECTOR, ".btn-lg")
