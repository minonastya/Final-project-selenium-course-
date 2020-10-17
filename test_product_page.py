from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages import data
import pytest

@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    # Arrange
    link = data.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.sign_in(data.MY_LOGIN, data.MY_PASSWORD)
    main_page = MainPage(browser, browser.current_url)
    main_page.search_product(data.NAME_OF_BOOK)
    main_page.go_to_product_page()
    product_page = ProductPage(browser, browser.current_url)
    #Act
    product_page.add_product_to_basket()
    #Assert
    product_page.product_added()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    # Arrange
    link = data.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.search_product(data.NAME_OF_BOOK)
    page.go_to_product_page()
    product_page = ProductPage(browser, browser.current_url)
    #Act
    product_page.add_product_to_basket()
    #Assert
    product_page.product_added()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # Arrange
    link = data.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.search_product(data.NAME_OF_BOOK)
    page.go_to_product_page()
    product_page = ProductPage(browser, browser.current_url)
    # Act
    product_page.go_to_login_page()
    #Assert
    product_page.login_page_is_open()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Arrange
    link = data.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.search_product(data.NAME_OF_BOOK)
    page.go_to_product_page()
    product_page = ProductPage(browser, browser.current_url)
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    #Assert
    basket_page.basket_is_empty()




