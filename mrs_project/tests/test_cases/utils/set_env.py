from selenium import webdriver

def select_webdriver(browser_type='chrome'):
    if browser_type.lower() == 'chrome':
        return webdriver.Chrome()
    elif browser_type.lower() == 'firefox':
        return webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser type: {browser_type}")
    
def close_driver(driver):
    driver.close()

def quit_driver(driver):
    driver.quit()