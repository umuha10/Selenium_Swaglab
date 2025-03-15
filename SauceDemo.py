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

    product_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price") #collect all product prices
    price_list = [float(price.text.replace("$", "")) for price in product_prices] #konversi harga kedalam angka float untuk dibandingkan
    sorted_correctly = price_list == sorted(price_list) #validasi apakah harga sudah diurutkan dari yang terendah ke tertinngi

    log_result("TC_014", True, sorted_correctly)

    # TC_015 User sort product by name (Z to A) (Possitive case)
    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_value("za")
    time.sleep(2)

    product_names = driver.find_elements(By.CLASS_NAME, "inventory_item_name") #collect all product names
    name_list = [name.text for name in product_names] #extracts the text from each webelement
    sorted_correctly = name_list == sorted(name_list, reverse=True) #sorts the list in ascending order (Z-A) by default.

    log_result("TC_015", True, sorted_correctly)

    # TC_016 User sort product by name (A to Z) (Possitive case)
    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_value("az")
    time.sleep(2)

    product_names = driver.find_elements(By.CLASS_NAME, "inventory_item_name") #collect all product names
    name_list = [name.text for name in product_names] #extracts the text from each webelement
    sorted_correctly = name_list == sorted(name_list) #sorts the list in ascending order (A-Z) by default.

    log_result("TC_016", True, sorted_correctly)

    # -------------------------------------
    # | VERIFY PRODUCT PAGE FUNCTIONALITY |
    # -------------------------------------

    # TC_017 User add product to cart (Possitive case)
    product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(1) > div.pricebar > button").click()
    time.sleep(2)
    product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(2) > div.pricebar > button").click()
    time.sleep(2)
    product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(3) > div.pricebar > button").click()
    time.sleep(2)
    product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(4) > div.pricebar > button").click()
    time.sleep(2)
    product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(5) > div.pricebar > button").click()
    time.sleep(2)
    product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(6) > div.pricebar > button").click()
    time.sleep(2)

    #--1 validate the cart icon update with item count
    cart_bedge = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a > span").text
    expected_cart_count = "6"
    log_result("TC_017 (1)", expected_cart_count, cart_bedge)

    #--2 validate the "Add to Cart" button changes to "Remove"
    actual_btn = driver.find_element(By.CSS_SELECTOR,"#inventory_container > div > div:nth-child(2) > div.pricebar > button").text
    expected_btn = "REMOVE"
    log_result("TC_017 (2)", expected_btn, actual_btn)

    # TC_018 User remove product from cart (Possitive case)
    product_remove = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(1) > div.pricebar > button").click()
    time.sleep(2)
    product_remove = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(2) > div.pricebar > button").click()
    time.sleep(2)
    product_remove = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(3) > div.pricebar > button").click()
    time.sleep(2)
    product_remove = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(4) > div.pricebar > button").click()
    time.sleep(2)
    product_remove = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(5) > div.pricebar > button").click()
    time.sleep(3)
    product_remove = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(6) > div.pricebar > button").click()
    time.sleep(2)

    #--1 validate the cart icon update with item count
    def check_element_presence(driver, selector, test_case):
        try:
            driver.find_element(By.CSS_SELECTOR, selector)
            log_result(test_case, "Not Present", "Present")
        except NoSuchElementException:
            log_result(test_case, "Not Present", "Not Present")

    check_element_presence(driver, "#shopping_cart_container > a > span", "TC_018 (1)")

    #--2 validate the "Remove"  button changes to "Add to Cart"
    actual_btn = driver.find_element(By.CSS_SELECTOR,"#inventory_container > div > div:nth-child(2) > div.pricebar > button").text
    expected_btn = "ADD TO CART"
    log_result("TC_018 (2)", expected_btn, actual_btn)

    # ---------------------------------------
    # | VERIFY PRODUCT DETAIL FUNCTIONALITY |
    # ---------------------------------------

    # TC_019 User open the product (Possitive Case)
    product_detail = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    product_name_expected = product_detail.text
    product_detail.click()
    time.sleep(2)

    #- The user is redirected to the product details page.
    actual_url = driver.current_url
    expected_url = "https://www.saucedemo.com/v1/inventory-item.html?id=4"
    log_result("TC_019 (1)", expected_url, actual_url)

    #- The page displays the product name, description, price, and an "Add to Cart" button.
    product_name_element = driver.find_element(By.CLASS_NAME, "inventory_details_name")
    product_name_displayed = product_name_element.is_displayed()
    log_result("TC_019 (2.1)", True, product_name_displayed)

    description = driver.find_element(By.CLASS_NAME, "inventory_details_desc").text
    log_result("TC_019 (2.2)", bool(description), True)

    product_price = driver.find_element(By.CLASS_NAME, "inventory_details_price").text
    log_result("TC_019 (2.3)", bool(product_price), True)

    expected_btn = "ADD TO CART"
    actual_btn = driver.find_element(By.CSS_SELECTOR, "#inventory_item_container > div > div > div > button").text
    log_result("TC_019 (2.4)", expected_btn, actual_btn)

    # - The product image is visible.
    product_img = driver.find_element(By.CLASS_NAME, "inventory_details_img")
    displayed_img = product_img.is_displayed()
    log_result("TC_019 (3)", True, displayed_img)

    # TC_20 User add product to cart (Possitive Case)
    product_detail_add = driver.find_element(By.CSS_SELECTOR, "#inventory_item_container > div > div > div > button")
    product_detail_add.click()
    time.sleep(2)

    # - The product is successfully added to the cart.
    # - The cart icon in the top-right corner updates to reflect the new item count.
    cart_bedge = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a > span").text
    expected_cart_count = "1"
    log_result("TC_020 (1)", expected_cart_count, cart_bedge)

    # - The "Add to Cart" button changes to "Remove."
    actual_btn = driver.find_element(By.CSS_SELECTOR,"#inventory_item_container > div > div > div > button").text
    expected_btn = "REMOVE"
    log_result("TC_020 (2)", expected_btn, actual_btn)

    # TC_21 User remove product from cart (Possitive Case)
    product_detail_remove = driver.find_element(By.CSS_SELECTOR, "#inventory_item_container > div > div > div > button")
    product_detail_remove.click()
    time.sleep(2)

    def check_element_presence(driver, selector, test_case):
        try:
            driver.find_element(By.CSS_SELECTOR, selector)
            log_result(test_case, "Not Present", "Present")
        except NoSuchElementException:
            log_result(test_case, "Not Present", "Not Present")
    check_element_presence(driver, "#shopping_cart_container > a > span", "TC_021 (1)")

    # TC_22 User back to product page (Possitive Case)
    product_detail_back = driver.find_element(By.CLASS_NAME, "inventory_details_back_button")
    product_detail_back.click()
    time.sleep(2)

    expected_url = "https://www.saucedemo.com/v1/inventory.html"
    actual_url = driver.current_url
    log_result("TC_022", expected_url, actual_url)

    # ----------------------------------------
    # | VERIFY "YOUR CART" PAGE FUNCTIONALITY|
    # ----------------------------------------

    # TC_023 User open the cart (Possitive Case)
    shopping_cart = driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container > a > svg")
    shopping_cart.click()
    time.sleep(2)

    expected_url = "https://www.saucedemo.com/v1/cart.html"
    actual_url = driver.current_url
    log_result("TC_023", expected_url, actual_url)

    # TC_026 User checkout with empties product (Possitive Case)
    checkout = driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button")
    checkout.click()
    time.sleep(2)

    expected_url = "https://www.saucedemo.com/v1/cart.html"
    actual_url = driver.current_url
    log_result("TC_026", expected_url, actual_url)
    
    # TC_024 User back to product page with click "continue shopping" button (Possitive Case)
    shopping_cart = driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container > a > svg")
    shopping_cart.click()
    time.sleep(2)
    
    continue_shopping = driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_footer > a.btn_secondary")
    continue_shopping.click()
    time.sleep(2)

    expected_url = "https://www.saucedemo.com/v1/inventory.html"
    actual_url = driver.current_url
    log_result("TC_024", expected_url, actual_url)

    #-----Add product for test-----
    product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(1) > div.pricebar > button")
    product_add.click()
    time.sleep(2)

    product_name_element = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link > div")
    product_name_displayed = product_name_element.is_displayed()
    log_result("TC_023 (1.1)", True, product_name_displayed)

    product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(4) > div.pricebar > button")
    product_add.click()
    time.sleep(2)

    product_name_element = driver.find_element(By.CSS_SELECTOR, "#item_5_title_link > div")
    product_name_displayed = product_name_element.is_displayed()
    log_result("TC_023 (1.2)", True, product_name_displayed)

    product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(2) > div.pricebar > button")
    product_add.click()
    time.sleep(2)

    product_name_element = driver.find_element(By.CSS_SELECTOR, "#item_0_title_link > div")
    product_name_displayed = product_name_element.is_displayed()
    log_result("TC_023 (1.3)", True, product_name_displayed)

    # TC_025 User remove product from cart (Possitive Case)
    shopping_cart = driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container > a > svg")
    shopping_cart.click()
    time.sleep(2)

    shopping_detail_remove = driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_list > div:nth-child(4) > div.cart_item_label > div.item_pricebar > button")
    shopping_detail_remove.click()
    time.sleep(2)

    try:
        actual_item = driver.find_element(By.CSS_SELECTOR,"#item_5_title_link > div")
        item_removed = False
    except:
        item_removed = True
    
    expected_removed = True
    log_result("TC_018 (2)", expected_removed, item_removed)

    # TC_027 User checkout with product added (Possitive Case)
    checkout = driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button")
    checkout.click()
    time.sleep(2)

    expected_url = "https://www.saucedemo.com/v1/checkout-step-one.html"
    actual_url = driver.current_url
    log_result("TC_027 (1)", expected_url, actual_url)

    try:
        first_name = driver.find_element(By.ID, "first-name")
        first_name_displayed = True

        last_name = driver.find_element(By.ID, "last-name")
        last_name_displayed = True
        
        postal_code = driver.find_element(By.ID, "last-name")
        postal_code_displayed = True

        btn_continue = driver.find_element(By.CSS_SELECTOR, "#checkout_info_container > div > form > div.checkout_buttons > input")
        btn_continue_displayed = True

        btn_cancel = driver.find_element(By.CSS_SELECTOR, "#checkout_info_container > div > form > div.checkout_buttons > a")
        btn_cancel_displayed = True
    except:
        first_name_displayed = False
        last_name_displayed = False
        postal_code_displayed = False
        btn_continue_displayed = False
        btn_cancel_displayed = False

    expected_first_name_displayed = True
    expected_last_name_displayed = True
    expected_postal_code_displayed = True
    expected_btn_continue_displayed = True
    expected_btn_cancel_displayed = True
    
    log_result("TC_027 (2)", expected_first_name_displayed, first_name_displayed)
    log_result("TC_027 (3)", expected_first_name_displayed, first_name_displayed)
    log_result("TC_027 (4)", expected_first_name_displayed, first_name_displayed)
    log_result("TC_027 (5)", expected_btn_continue_displayed, btn_continue_displayed)
    log_result("TC_027 (6)", expected_btn_cancel_displayed, btn_cancel_displayed)

    # Add more test cases with similar logging
    # ...

finally:
    driver.quit()