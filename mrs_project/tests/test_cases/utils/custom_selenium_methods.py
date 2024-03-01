# selenium_utils.py
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def launch_url(driver, url):
    driver.get(url)

def is_successful_navigation(driver, expected_title):
    actual_title = driver.title
    if(actual_title == expected_title):
        print("User navigated successfully to the page: "+{expected_title})
    else:
        print("User failed to navigate successfully to the page: "+{expected_title})

def maximize_browser(driver):
    driver.maximize_window()

def click_element(driver, locator):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    element.click()

def fiil_field(driver, locator, keys):
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
    element.send_keys(keys)

def select_from_dropdown(driver, locator, value):
    select = Select(driver.find_element(*locator))
    select.select_by_value(value)

def click_radio_button(driver, locator):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    element.click()

def check_checkbox(driver, locator):
    checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    if not checkbox.is_selected():
        checkbox.click()

def uncheck_checkbox(driver, locator):
    checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    if checkbox.is_selected():
        checkbox.click()
    
def wait_for(seconds=5):
    time.sleep(seconds)
