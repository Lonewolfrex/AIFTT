import pytest
from selenium import webdriver
from utils.custom_selenium_methods import *
from utils.set_env import *

@pytest.fixture(scope="module", params=["firefox","chrome"])
def select_webdriver(request):
    if request.param.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif request.param.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser type: {request.param}")    
    
    yield driver
    quit_driver(driver);
    
def test_1(select_webdriver):
    driver=select_webdriver;
    maximize_browser(driver);
    try:
        launch_url(driver, "https://demo.openmrs.org/openmrs/login.htm");
        fiil_field(driver, (By.ID, "username"),"admin");
        fiil_field(driver, (By.ID, "password"),"Admin123");
        click_element(driver, (By.ID, "Registration Desk"));
        click_element(driver, (By.ID, "loginButton"));
        wait_for(3);
        click_element(driver, (By.XPATH, "//i[@class='icon-signout small']"));
        wait_for(2);       
    finally:
        close_driver(driver);

