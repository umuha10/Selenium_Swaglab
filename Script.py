from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Path ke WebDriver (sesuaikan dengan lokasi file chromedriver)
driver = webdriver.Chrome()


# Buka halaman website
driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()

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

# TC_002 User empties username (Negative Case)
driver.refresh()
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(2)

# TC_003 User empties password (Negative Case)
driver.refresh()
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")

password_field= driver.find_element(By.ID, "password")
password_field.send_keys("")

login_button = driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# TC_004 User fills in correct username and wrong password (Negative Case)
driver.refresh()
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("123")

login_button = driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# TC_005 User fills in wrong username and correct password (Negative Case)
driver.refresh()
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("wrong")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# TC_006 User fills username with locked-out user (Negative Case)
driver.refresh()
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("locked_out_user")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# TC_007 User fills in correct username and password (Possitive Case)
driver.refresh()
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(2)

# -------------------------------
# | VERIFY SIDEBAR FUNCTIONALITY|
# -------------------------------

# TC_008 User click button "Reset App State" (Positive case)
burger_button = driver.find_element(By.CLASS_NAME, "bm-burger-button")
burger_button.click()

wait = WebDriverWait(driver, 10) #--menunggu sampai element tampil
reset_app = wait.until(EC.element_to_be_clickable((By.ID, "reset_sidebar_link")))
reset_app.click()
time.sleep(2)

# TC_009 User click button icon close (Possitive case)
close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bm-cross-button")))
close_button.click()

# TC_010 User click button "About" (Possitive case)
burger_button = driver.find_element(By.CLASS_NAME, "bm-burger-button")
burger_button.click()

wait = WebDriverWait(driver, 10)
about_button = wait.until(EC.element_to_be_clickable((By.ID, "about_sidebar_link")))
about_button.click()

driver.back()
time.sleep(2)

# TC_011 User click button "All Items" (Possitive case)
wait = WebDriverWait(driver, 10)
all_item = wait.until(EC.element_to_be_clickable((By.ID, "inventory_sidebar_link")))
all_item.click()
time.sleep(2)

# TC_012 User click button "Logout" (Possitive case)
burger_button = driver.find_element(By.CLASS_NAME, "bm-burger-button")
burger_button.click()

logout_button = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
logout_button.click()
time.sleep(2)

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

# TC_014 User sort product by price (low to high) (Possitive case)
dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
dropdown.select_by_value("lohi")
time.sleep(2)

# TC_015 User sort product by name (Z to A) (Possitive case)
dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
dropdown.select_by_value("za")
time.sleep(2)

# TC_016 User sort product by name ((A to Z) (Possitive case)
dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
dropdown.select_by_value("az")
time.sleep(2)

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

# ---------------------------------------
# | VERIFY PRODUCT DETAIL FUNCTIONALITY |
# ---------------------------------------

# TC_019 User open the product (Possitive Case)
product_detail = driver.find_element(By.CLASS_NAME, "inventory_item_name")
product_detail.click()
time.sleep(2)

# TC_20 User add product to cart (Possitive Case)
product_detail_add = driver.find_element(By.CSS_SELECTOR, "#inventory_item_container > div > div > div > button")
product_detail_add.click()
time.sleep(2)

# TC_21 User remove product from cart (Possitive Case)
product_detail_remove = driver.find_element(By.CSS_SELECTOR, "#inventory_item_container > div > div > div > button")
product_detail_remove.click()
time.sleep(2)

# TC_22 User back to product page (Possitive Case)
product_detail_back = driver.find_element(By.CLASS_NAME, "inventory_details_back_button")
product_detail_back.click()
time.sleep(2)

# ----------------------------------------
# | VERIFY "YOUR CART" PAGE FUNCTIONALITY|
# ----------------------------------------

# TC_023 User open the cart (Possitive Case)
shopping_cart = driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container > a > svg")
shopping_cart.click()
time.sleep(2)

# TC_026 User checkout with empties product (Possitive Case)
checkout = driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button")
checkout.click()
time.sleep(2)

# TC_024 User back to product page with click "continue shopping" button (Possitive Case)
shopping_cart = driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container > a > svg")
shopping_cart.click()
time.sleep(2)

continue_shopping = driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_footer > a.btn_secondary")
continue_shopping.click()
time.sleep(2)

#-----Add product for test-----
product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(1) > div.pricebar > button")
product_add.click()
time.sleep(2)

product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(4) > div.pricebar > button")
product_add.click()
time.sleep(2)

product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(2) > div.pricebar > button")
product_add.click()
time.sleep(2)

# TC_025 User remove product from cart (Possitive Case)
shopping_cart = driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container > a > svg")
shopping_cart.click()
time.sleep(2)

shopping_detail_remove = driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_list > div:nth-child(4) > div.cart_item_label > div.item_pricebar > button")
shopping_detail_remove.click()
time.sleep(2)

# TC_027 User checkout with product added (Possitive Case)
checkout = driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button")
checkout.click()
time.sleep(2)

# ----------------------------------------------------------
# | VERIFY "CHECKOUT: YOUR INFORMATION" PAGE FUNCTIONALITY |
# ----------------------------------------------------------

# TC_028 User cancel checkout product (Possitive Case)
cancel_checkout = driver.find_element(By.CSS_SELECTOR, "#checkout_info_container > div > form > div.checkout_buttons > a")
cancel_checkout.click()




#Melanjutkan ke halaman checkout:your information
checkout = driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button")
checkout.click()

# Send Information (Negatif Case #) --semua fiel dikosongkan
first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("")

last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("")

postal_code = driver.find_element(By.ID, "postal-code")
postal_code.send_keys("")

continue_checkout = driver.find_element(By.CSS_SELECTOR, "#checkout_info_container > div > form > div.checkout_buttons > input")
continue_checkout.click()

# Send Information (Negative case #) --hanya nama depan yang diisi
first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("lala")

continue_checkout = driver.find_element(By.CSS_SELECTOR, "#checkout_info_container > div > form > div.checkout_buttons > input")
continue_checkout.click()

time.sleep(2)

# -- hanya nama belakang yang diisi
driver.refresh()
last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("lala")

continue_checkout = driver.find_element(By.CSS_SELECTOR, "#checkout_info_container > div > form > div.checkout_buttons > input")
continue_checkout.click()

time.sleep(2)

# -- hanya post code yang diisi
driver.refresh()

postal_code = driver.find_element(By.ID, "postal-code")
postal_code.send_keys("123")

continue_checkout = driver.find_element(By.CSS_SELECTOR, "#checkout_info_container > div > form > div.checkout_buttons > input")
continue_checkout.click()

time.sleep(2)

# Send Information (Possitive Case #)
driver.refresh()
first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("Salsa")

last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("Khairina")

postal_code = driver.find_element(By.ID, "postal-code")
postal_code.send_keys("56768")
time.sleep(2)

continue_checkout = driver.find_element(By.CSS_SELECTOR, "#checkout_info_container > div > form > div.checkout_buttons > input")
continue_checkout.click()

# Finish Shopping
finish_shopping = driver.find_element(By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.cart_footer > a.btn_action.cart_button")
finish_shopping.click()

input("tekan enter untuk keluar...")

# Tunggu beberapa detik lalu tutup browser
driver.quit()
