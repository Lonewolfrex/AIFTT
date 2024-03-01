import pytest
from selenium import webdriver
from utils.custom_selenium_methods import *
from utils.set_env import *
class HomePage:
    def __init__(self, driver, session_id):
        self.driver = driver
        self.btn_logout = (By.XPATH, "//i[@class='icon-signout small']")
        self.dropdown_session = (By.ID, "selected-location")

    def perform_logout_action(self):
        driver=self.driver;
        click_element(driver, self.btn_logout);
        wait_for(2);  
        