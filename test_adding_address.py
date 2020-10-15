from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages import data

def test_success_adding_address(browser):
    link = data.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.sign_in(data.MY_LOGIN, data.MY_PASSWORD)
    login_page.success_login()
    main_page = MainPage(browser, browser.current_url)
    main_page.go_to_profile()
    account_page = AccountPage(browser, browser.current_url)
    account_page.select_address_book()
    account_page.add_new_address()
