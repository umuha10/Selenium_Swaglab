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
    with open("test_report.txt", "a") as report_file:
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

    check_element_presence(driver, "#shopping_cart_container > a > span", "TC_008 (1)")

    # --Compare expected and actual results (2)
    filter_clear = driver.find_element(By.CLASS_NAME, "product_sort_container")
    expected_filter = "az"
    actual_filter = filter_clear.get_attribute("value")
    log_result("TC_008 (2)", expected_filter, actual_filter)
    
    # TC_009 User click button icon close (Possitive case)
    close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bm-cross-button")))
    close_button.click()
    time.sleep(2)

    try:
        sidebar = driver.find_element(By.CLASS_NAME, "bm-menu-wrap")
        sidebar_closed = sidebar.is_displayed()
    except NoSuchElementException:
        sidebar_closed = True

    log_result("TC_009", True, sidebar_closed)

    # TC_010 User click button "About" (Possitive case)
    burger_button = driver.find_element(By.CLASS_NAME, "bm-burger-button")
    burger_button.click()

    wait = WebDriverWait(driver, 10)
    about_button = wait.until(EC.element_to_be_clickable((By.ID, "about_sidebar_link")))
    about_button.click()

    expected_url = "https://saucelabs.com/"
    actual_url = driver.current_url

    log_result("TC_010", expected_url, actual_url)

    driver.back()
    time.sleep(2)

    # TC_011 User click button "All Items" (Possitive case)
    wait = WebDriverWait(driver, 10)
    all_item = wait.until(EC.element_to_be_clickable((By.ID, "inventory_sidebar_link")))
    all_item.click()
    time.sleep(2)

    expected_text = "Products"
    actual_text = driver.find_element(By.CLASS_NAME, "product_label").text
    log_result("TC_011", expected_text, actual_text)

    # TC_012 User click button "Logout" (Possitive case)
    burger_button = driver.find_element(By.CLASS_NAME, "bm-burger-button")
    burger_button.click()

    logout_button = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
    logout_button.click()
    time.sleep(2)

    expected_logout = "https://www.saucedemo.com/v1/index.html"
    actual_logout = driver.current_url

    log_result("TC_012", expected_logout, actual_logout)

    # -----------------
    # | VERIFY FILTER |
    # -----------------

    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    time.sleep(2)

    # TC_013 User sort product by price (high to low) (Possitive case)
    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_value("hilo")
    time.sleep(2)

    product_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price") #-----ambil semua harga produk-----
    price_list = [float(price.text.replace("$", "")) for price in product_prices] #konversi harga kedalam angka float untuk dibandingkan
    sorted_correctly = price_list == sorted(price_list, reverse=True) #validasi apakah harga sudah diurutkan dari yang tertinggii ke terendah

    log_result("TC_013", True, sorted_correctly)

    # TC_014 User sort product by price (low to high) (Possitive case)
    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_value("lohi")
    time.sleep(2)

    product_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price") #-----ambil semua harga produk-----
    price_list = [float(price.text.replace("$", "")) for price in product_prices] #konversi harga kedalam angka float untuk dibandingkan
    sorted_correctly = price_list == sorted(price_list) #validasi apakah harga sudah diurutkan dari yang terendah ke tertinngi

    log_result("TC_014", True, sorted_correctly)

    # TC_015 User sort product by name (Z to A) (Possitive case)
    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_value("za")
    time.sleep(2)

    filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    expected_hl = "za"
    actual_hl = filter_dropdown.get_attribute("value")

    log_result("TC_015", expected_hl, actual_hl)

    # TC_016 User sort product by name ((A to Z) (Possitive case)
    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_value("az")
    time.sleep(2)

    filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    expected_hl = "az"
    actual_hl = filter_dropdown.get_attribute("value")

    log_result("TC_016", expected_hl, actual_hl)

    # Add more test cases with similar logging
    # ...

finally:
    driver.quit()