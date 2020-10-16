from .base_page import BasePage
from .locators import AccountPageLocators
from pages import data
from selenium.webdriver.support.ui import Select

class AccountPage(BasePage):
    def select_address_book(self):
        link = self.browser.find_element(*AccountPageLocators.ADDRESS_BOOK_TAB)
        link.click()

    def open_new_address_form(self):
        button = self.browser.find_element(*AccountPageLocators.ADD_NEW_ADDRESS)
        button.click()

    def add_new_address(self, appeal, first_name, last_name, first_line_address, second_line_address,\
                        third_line_address, city, state, postcode, country, phone, notes):
        new_appeal = Select(self.browser.find_element(*AccountPageLocators.APPEAL))
        new_first_name = self.browser.find_element(*AccountPageLocators.FIRST_NAME)
        new_last_name = self.browser.find_element(*AccountPageLocators.LAST_NAME)
        new_first_line_address = self.browser.find_element(*AccountPageLocators.FIRST_LINE_ADDRESS)
        new_second_line_address = self.browser.find_element(*AccountPageLocators.SECOND_LINE_ADDRESS)
        new_third_line_address = self.browser.find_element(*AccountPageLocators.THIRD_LINE_ADDRESS)
        new_city = self.browser.find_element(*AccountPageLocators.CITY)
        new_state = self.browser.find_element(*AccountPageLocators.STATE)
        new_postcode = self.browser.find_element(*AccountPageLocators.POSTCODE)
        new_country = Select(self.browser.find_element(*AccountPageLocators.COUNTRY))
        new_phone = self.browser.find_element(*AccountPageLocators.PHONE)
        new_notes = self.browser.find_element(*AccountPageLocators.NOTES)
        save_address_button = self.browser.find_element(*AccountPageLocators.SAVE_ADDRESS)

        new_appeal.select_by_index(appeal)
        new_first_name.send_keys(first_name)
        new_last_name.send_keys(last_name)
        new_first_line_address.send_keys(first_line_address)
        new_second_line_address.send_keys(second_line_address)
        new_third_line_address.send_keys(third_line_address)
        new_city.send_keys(city)
        new_state.send_keys(state)
        new_postcode.send_keys(postcode)
        new_country.select_by_visible_text(country)
        new_phone.send_keys(phone)
        new_notes.send_keys(notes)
        save_address_button.click()

    def address_added(self):
        assert data.ADD_ADDRESS_PATH not in self.browser.current_url, "No address added, check data"







