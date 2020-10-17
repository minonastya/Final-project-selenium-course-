from .base_page import BasePage
from .locators import ProductPageLocators
from pages import data

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def product_added(self):
        alert = self.browser.find_elements(*ProductPageLocators.ALERT)
        assert len(alert) > 0, "The item has not been added to the basket"

    def go_to_login_page(self):
        link = self.browser.find_element(*ProductPageLocators.LOGIN_LINK)
        link.click()

    def login_page_is_open(self):
        assert data.LOGIN_PATH in self.browser.current_url, "Login page is not open"

    def go_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()