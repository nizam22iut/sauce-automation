# pages/inventory_page.py
from base.base_page import BasePage
from locator.inventory_locators import InventoryLocators as L

class InventoryPage(BasePage):
    """Page object for the inventory (products) page."""

    def add_first_item_to_cart(self):
        buttons = self.driver.find_elements(*L.ADD_TO_CART_BUTTONS)
        if buttons:
            buttons[0].click()

    def go_to_cart(self):
        self.click(L.SHOPPING_CART_ICON)

    def get_item_count(self):
        items = self.driver.find_elements(*L.INVENTORY_ITEM)
        return len(items)
