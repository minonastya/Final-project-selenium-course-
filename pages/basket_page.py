from .base_page import BasePage
from .locators import BasketPageLocators
from pages import data
from selenium.common.exceptions import NoSuchElementException

class BasketPage(BasePage):
    def is_element_not_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return True
        return False

    def basket_is_empty(self):
        assert self.is_element_not_present(*BasketPageLocators.BUTTON_ORDERING), "Basket is not empty"