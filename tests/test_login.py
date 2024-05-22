import pytest
from pages.login_page import LoginPage


def test_login(browser):
    browser.get("https://www.saucedemo.com/")
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in browser.current_url
