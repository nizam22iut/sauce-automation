# Mandatory file for pytest
# When the pytest is run, it will first try to locate this file for starting the test


import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import allure


# This will read the data from the yaml file for the starting information like URL, browser
@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)


# initiate the browser before each test case, wait to complete the test, tead down and clean up
@pytest.fixture
def setup(request,config):

# initiate the browser before each test case
    browser=config.get("browser","firefox")

    if browser == "firefox":
        driver= webdriver.Firefox()

    elif browser == "chrome":
        driver = webdriver.Chrome()
        
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    

    driver.maximize_window()
    driver.implicitly_wait(config.get("implicit_wait",5))

    #wait to complete  the test
    yield driver

    # take screenshot in test failure
    if request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="failure_screenshot",
            attachment_type=allure.attachment_type.PNG
        )


    #tead down and clean up after each test
    driver.quit()
    

# setup for the allure report to take screehshot
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
