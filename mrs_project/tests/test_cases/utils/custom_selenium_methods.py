# selenium_utils.py
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import pytest

def launch_url(driver, url):
    driver.get(url)

def verify_successful_navigation(driver, expected_title):
    wait_for_page_load(driver)
    actual_title = driver.title
    if(actual_title == expected_title):
        print("User navigated successfully to the page: "+ str(expected_title))
    else:
        print("User failed to navigate successfully to the page: "+ str(expected_title))

def maximize_browser(driver):
    driver.maximize_window()

def click_element(driver, locator):
    webelement_exists(driver, locator)
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    element.click()

def fiil_field(driver, locator, keys):
    webelement_exists(driver, locator)
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
    element.clear()
    element.send_keys(keys)

def select_from_dropdown(driver, locator, value):
    webelement_exists(driver, locator)
    select = Select(driver.find_element(*locator))
    select.select_by_value(value)

def assert_value(expected_value, actual_value):
    try:
        assert expected_value == actual_value
    except AssertionError:
        raise AssertionError(f"Expected value '{expected_value}' does not match actual value '{actual_value}'")    

def click_radio_button(driver, locator):
    webelement_exists(driver, locator)
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    element.click()

def check_checkbox(driver, locator):
    webelement_exists(driver, locator)
    checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    if not checkbox.is_selected():
        checkbox.click()

def uncheck_checkbox(driver, locator):
    webelement_exists(driver, locator)
    checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    if checkbox.is_selected():
        checkbox.click()
    
def wait_for(seconds=5):
    time.sleep(seconds)

def wait_for_page_load(driver, timeout=30):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    
def webelement_exists(driver, locator):
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
        assert element is not None, "Element exists on the page"
    except NoSuchElementException:
        pytest.fail("Element does not exist on the page")