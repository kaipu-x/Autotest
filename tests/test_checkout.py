import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout(browser):
    browser.get("https://www.saucedemo.com/")
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(browser)
    checkout_page.fill_information_and_continue("John", "Doe", "12345")
    checkout_page.finish_checkout()

    assert "checkout-complete.html" in browser.current_url
