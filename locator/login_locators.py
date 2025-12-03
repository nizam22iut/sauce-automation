# according to the POM design putting only the page locators here in the locator files

# locators for the login page webelements
from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME=(By.ID,"user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
