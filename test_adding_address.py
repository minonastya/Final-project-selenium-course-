from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages import data
import pytest


def test_success_adding_address(browser):
    #Arrange
    link = data.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.sign_in(data.MY_LOGIN, data.MY_PASSWORD)
    main_page = MainPage(browser, browser.current_url)
    main_page.go_to_profile()
    account_page = AccountPage(browser, browser.current_url)
    #Act
    account_page.select_address_book()
    account_page.open_new_address_form()
    account_page.add_new_address(data.APPEAL, data.FIRST_NAME, data.LAST_NAME, data.FIRST_LINE_ADDRESS,\
                                 data.EMPTY_INPUT,data.EMPTY_INPUT, data.CITY, data.EMPTY_INPUT, data.POSTCODE,\
                                 data.COUNTRY,data.EMPTY_INPUT, data.EMPTY_INPUT)
    #Assert
    account_page.address_added()
