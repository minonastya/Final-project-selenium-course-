from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages import data

def test_success_registration(browser):
    link = data.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.sign_up(data.NEW_LOGIN_TC1, data.NEW_PASSWORD1_TC1, data.NEW_PASSWORD2_TC1)
    login_page.success_registration()

def test_different_passwords(browser):
    link = data.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.sign_up(data.NEW_LOGIN_TC2, data.NEW_PASSWORD1_TC2, data.NEW_PASSWORD2_TC2)
    login_page.success_registration()

def test_insecure_password(browser):
    link = data.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.sign_up(data.NEW_LOGIN_TC3, data.NEW_PASSWORD1_TC3, data.NEW_PASSWORD2_TC3)
    login_page.success_registration()