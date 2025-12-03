# pages/cart_page.py
from base.base_page import BasePage
from locator.cart_locators import CartLocators as C, CheckoutLocators as CH

class CartPage(BasePage):
    """Cart page object with checkout actions."""

    def click_checkout(self):
        self.click(C.CHECKOUT_BUTTON)

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.type(CH.FIRST_NAME, first_name)
        self.type(CH.LAST_NAME, last_name)
        self.type(CH.POSTAL_CODE, postal_code)
        self.click(CH.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(CH.FINISH_BUTTON)

    def is_order_successful(self):
        return self.driver.find_element(*CH.SUCCESS_MESSAGE).is_displayed()
