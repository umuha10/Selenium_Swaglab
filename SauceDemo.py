from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException

# Initialize the driver
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()

# Define the log_result function
def log_result(test_case, expected, actual):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    result = "Passed" if expected == actual else f"Failed - Expected: '{expected}', Actual: '{actual}'"
    with open("test_report2.txt", "a") as report_file:
        report_file.write(f"[{timestamp}] {test_case}: {result}\n")

# Example test case with logging
try:
    # ---------
    # | LOGIN |
    # ---------

    # TC_001 User empties username and password (Negative Case)
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(2)

    # --Compare expected and actual results
    expected_validation = "Epic sadface: Username is required"
    actual_validation = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > h3").text
    log_result("TC_001", expected_validation, actual_validation)

    # TC_002 User empties username (Negative Case)
    driver.refresh()
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(2)

    # --Compare expected and actual results
    expected_validation = "Epic sadface: Username is required"
    actual_validation = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > h3").text
    log_result("TC_002", expected_validation, actual_validation)

    # TC_003 User empties password (Negative Case)
    driver.refresh()
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")

    password_field= driver.find_element(By.ID, "password")
    password_field.send_keys("")

    login_button = driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # --Compare expected and actual results
    expected_validation = "Epic sadface: Password is required"
    actual_validation = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > h3").text
    log_result("TC_003", expected_validation, actual_validation)

    # TC_004 User fills in correct username and wrong password (Negative Case)
    driver.refresh()
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("123")

    login_button = driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # --Compare expected and actual results
    expected_validation = "Epic sadface: Username and password do not match any user in this service"
    actual_validation = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > h3").text
    log_result("TC_004", expected_validation, actual_validation)

    # TC_005 User fills in wrong username and correct password (Negative Case)
    driver.refresh()
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("wrong")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # --Compare expected and actual results
    expected_validation = "Epic sadface: Username and password do not match any user in this service"
    actual_validation = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > h3").text
    log_result("TC_005", expected_validation, actual_validation)

    # TC_006 User fills username with locked-out user (Negative Case)
    driver.refresh()
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("locked_out_user")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # --Compare expected and actual results
    expected_validation = "Epic sadface: Sorry, this user has been locked out."
    actual_validation = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > h3").text
    log_result("TC_006", expected_validation, actual_validation)

    # TC_007 User fills in correct username and password (Positive Case)
    driver.refresh()
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(2)

    # --Compare expected and actual results
    expected_text = "Products"
    actual_text = driver.find_element(By.CLASS_NAME, "product_label").text
    log_result("TC_007", expected_text, actual_text)

    # -------------------------------
    # | VERIFY SIDEBAR FUNCTIONALITY|
    # -------------------------------

    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_value("hilo")
    time.sleep(2)

    product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(1) > div.pricebar > button").click()
    time.sleep(2)
    product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(2) > div.pricebar > button").click()
    time.sleep(2)

    # TC_008 User click button "Reset App State" (Positive case)
    burger_button = driver.find_element(By.CLASS_NAME, "bm-burger-button")
    burger_button.click()

    wait = WebDriverWait(driver, 10) #--menunggu sampai element tampil
    reset_app = wait.until(EC.element_to_be_clickable((By.ID, "reset_sidebar_link")))
    reset_app.click()
    time.sleep(2)

    # --Compare expected and actual results (1)
    def check_element_presence(driver, selector, test_case):
        try:
            driver.find_element(By.CSS_SELECTOR, selector)
            log_result(test_case, "Not Present", "Present")
        except NoSuchElementException:
            log_result(test_case, "Not Present", "Not Present")

    # Example usage
    check_element_presence(driver, "#shopping_cart_container > a > span", "TC_008 (1)")

    # --Compare expected and actual results (1)
    filter_clear = driver.find_element(By.CLASS_NAME, "product_sort_container")
    expected_filter = "az"
    actual_filter = filter_clear.get_attribute("value")
    log_result("TC_008 (2)", expected_filter, actual_filter)
    
    
    # Add more test cases with similar logging
    # ...

finally:
    driver.quit()