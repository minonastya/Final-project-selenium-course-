from .base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_profile(self):
        link = self.browser.find_element(*MainPageLocators.PROFILE_LINK)
        link.click()

    def search_product(self, product_name):
        search_input = self.browser.find_element(*MainPageLocators.SEARCH_INPUT)
        search_button = self.browser.find_element(*MainPageLocators.SEARCH_BUTTON)
        search_input.send_keys(product_name)
        search_button.click()

    def go_to_product_page(self):
        img_book = self.browser.find_element(*MainPageLocators.IMAGE_OF_PRODUCT)
        self.browser.execute_script("window.scrollBy(0, 100);")
        img_book.click()
