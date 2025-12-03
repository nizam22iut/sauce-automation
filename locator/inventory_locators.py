# locators for the inventory page webelements

from selenium.webdriver.common.by import By

class InventoryLocators:
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button.btn_inventory")
    SHOPPING_CART_ICON = (By.ID, "shopping_cart_container")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
