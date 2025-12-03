# tests/test_checkout.py
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import json
import time


def load_users():
    with open("data/users.json") as f:
        return json.load(f)

def test_checkout_single_item(setup, config):
    users = load_users()
    valid = users["valid_user"]

    login_page = LoginPage(setup)
    login_page.open(config["base_url"])
    login_page.login(valid["username"], valid["password"])

    inventory_page = InventoryPage(setup)
    assert inventory_page.get_item_count() > 0

    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()
    

    assert "cart.html" in setup.current_url

    cart_page = CartPage(setup)
    cart_page.click_checkout()
    cart_page.fill_checkout_info("Sam", "Uddin", "70508")
    cart_page.finish_checkout()

    assert cart_page.is_order_successful()
