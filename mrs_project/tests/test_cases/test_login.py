import pytest
from selenium import webdriver
from utils.custom_selenium_methods import *
from utils.set_env import *
from pages.login_pg import *
from pages.home_pg import *

@pytest.fixture(scope="function", params=["firefox"], autouse=True)
def select_webdriver(request):
    if request.param.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif request.param.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser type: {request.param}")    
    maximize_browser(driver);
    
    yield driver
    close_driver(driver);
    quit_driver(driver);

@pytest.mark.parametrize("username, password, session_id", [
("admin","Admin123","Inpatient Ward"),
("admin","Admin123","Isolation Ward"),
("admin","Admin123","Laboratory"),
("admin","Admin123","Outpatient Clinic"),
("admin","Admin123","Pharmacy"),
("admin","Admin123","Registration Desk"),
])    
def test_successful_login(select_webdriver,username,password,session_id):
    driver=select_webdriver;
    # maximize_browser(driver);

    login_page = LoginPage(driver,session_id)
    home_page = HomePage(driver,session_id)
    
    login_page.open_login_page()
    # is_successful_navigation(driver,"Login")
    login_page.perform_login_action(username,password)
    # is_successful_navigation(driver,"Home")
    home_page.perform_logout_action()
    # is_successful_navigation(driver,"Login")      