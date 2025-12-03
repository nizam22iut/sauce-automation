# file contains real test cases and the program starts here. Program starting point is with the pytest

from pages.login_page import LoginPage
import json


# load user data file for running the test case with
def load_users():

    with open("data/users.json") as f:
        return json.load(f)
    
# test case- checking with valid user login
def test_valid_login(setup, config):
    users = load_users()
    valid = users["valid_user"]

    login_page = LoginPage(setup)
    login_page.open(config["base_url"])
    login_page.login(valid["username"], valid["password"])

    # After successful login, URL should contain "inventory"
    assert "inventory" in setup.current_url

# test case- checking with locker user trying to login
def test_invalid_login_locked_user(setup, config):
    users = load_users()
    invalid = users["invalid_user"]

    login_page = LoginPage(setup)
    login_page.open(config["base_url"])
    login_page.login(invalid["username"], invalid["password"])

    error_text = login_page.get_error_message()
    assert "Sorry, this user has been locked out" in error_text