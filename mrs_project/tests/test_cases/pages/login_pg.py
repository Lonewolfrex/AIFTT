import pytest
from selenium import webdriver
from utils.custom_selenium_methods import *
from utils.set_env import *
class LoginPage:
    def __init__(self, driver, session_id):
        self.driver = driver
        self.url = "https://demo.openmrs.org/openmrs/login.htm"
        self.txt_field_username = (By.ID, "username")
        self.txt_field_password = (By.ID, "password")
        self.btn_session = (By.ID, session_id)
        self.btn_login = (By.ID, "loginButton")

    def open_login_page(self):
        self.driver.get(self.url)

    def perform_login_action(self, username, password):
        driver=self.driver;
        fiil_field(driver, self.txt_field_username,username);
        fiil_field(driver, self.txt_field_password,password);
        click_element(driver, self.btn_session);
        click_element(driver, self.btn_login);
        wait_for(3);  
        