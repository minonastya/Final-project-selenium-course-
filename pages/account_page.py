from .base_page import BasePage
from .locators import AccountPageLocators
from pages import data

class AccountPage(BasePage):
    def select_address_book(self):
        link = self.browser.find_element(*AccountPageLocators.ADDRESS_BOOK_TAB)
        link.click()

    def add_new_address(self):
        button = self.browser.find_element(*AccountPageLocators.ADD_NEW_ADDRESS)
        button.click()

