# according to my POM design, putting the page operations here. Login page will take login operation
# If login fails shows error message

from base.base_page import BasePage
from locator.login_locators import LoginLocators as L


class LoginPage(BasePage):


    def open(self,base_url):
        self.driver.get(base_url)


    def login(self,username,password):
        self.type(L.USERNAME, username)
        self.type(L.PASSWORD, password)
        self.click(L.LOGIN_BUTTON)


    def get_error_message(self):
        
        return self.driver.find_element(*L.ERROR_MESSAGE).text
        
    
    
    

    



