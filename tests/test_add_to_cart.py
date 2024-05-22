import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_to_cart(browser):
    browser.get("https://www.saucedemo.com/")
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_to_cart()
    inventory_page.go_to_cart()

    assert "cart.html" in browser.current_url
