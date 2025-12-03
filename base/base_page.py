#define the basic actions for a webpage like finding element, click, send keys to a field

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait= WebDriverWait(self.driver,timeout)



    def find(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    

    def click(self, locator):
        """Wait until clickable, then click."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text, clear_first=True):
        """Type text into an input field."""
        element = self.find(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get element text."""
        return self.find(locator).get_text()

    def is_visible(self, locator):
        """Return True if element becomes visible, else False."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False
