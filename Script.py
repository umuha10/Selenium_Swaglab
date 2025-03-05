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

# Login (Negative Case #1)
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("umu")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("habibah")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(2)

# Login (Negative Case #2)
driver.refresh()
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("umu")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(2)

# Login (Negative Case #3)
driver.refresh()
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")

password_field= driver.find_element(By.ID, "password")
password_field.send_keys("123")

login_button = driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Login (Negative Case #4)
driver.refresh()
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("")

login_button = driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Login (Possitive Case #5)
driver.refresh
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button").click()

# ------------------------
# | VERIFY BUTTON BURGER |
# ------------------------

# Button link All Item (Positive case #6)
burger_button = driver.find_element(By.CLASS_NAME, "bm-burger-button")
burger_button.click()

# Button link All item (Possitive case #7)
wait = WebDriverWait(driver, 10)
all_item = wait.until(EC.element_to_be_clickable((By.ID, "inventory_sidebar_link")))
all_item.click()

# Button link All item (Possitive case #8)
burger_button = driver.find_element(By.CLASS_NAME, "bm-burger-button")
burger_button.click()

wait = WebDriverWait(driver, 10)
about_button = wait.until(EC.element_to_be_clickable((By.ID, "about_sidebar_link")))
about_button.click()

driver.back()
time.sleep(2)

# Button icon close (Possitive case #9)
close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bm-cross-button")))
close_button.click()

# Button logout (Possitive case #10)
burger_button = driver.find_element(By.CLASS_NAME, "bm-burger-button")
burger_button.click()

logout_button = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
logout_button.click()

# -----------------
# | VERIFY FILTER |
# -----------------

# Dropdown filter (Possitive case #11)
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

time.sleep(2)

dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
dropdown.select_by_value("hilo")
time.sleep(2)

dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
dropdown.select_by_value("lohi")
time.sleep(2)

dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
dropdown.select_by_value("za")
time.sleep(2)

dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
dropdown.select_by_value("az")
time.sleep(2)

# ------------------
# | PRODUCT DETAIL |
# ------------------
# Product detail (Possitive case #12)
product_detail = driver.find_element(By.CLASS_NAME, "inventory_item_name")
product_detail.click()
time.sleep(2)

product_detail_add = driver.find_element(By.CSS_SELECTOR, "#inventory_item_container > div > div > div > button")
product_detail_add.click()
time.sleep(2)

product_detail_remove = driver.find_element(By.CSS_SELECTOR, "#inventory_item_container > div > div > div > button")
product_detail_remove.click()
time.sleep(2)

product_detail_back = driver.find_element(By.CLASS_NAME, "inventory_details_back_button")
product_detail_back.click()
time.sleep(2)

# --------------------------
# | PRODUCT ADD AND REMOVE |
# --------------------------
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

# ------------------------
# | VERIFY SHOPPING DETAIL |
# ------------------------

shopping_cart = driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container > a > svg")
shopping_cart.click()

continue_shopping = driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_footer > a.btn_secondary")
continue_shopping.click()

product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(1) > div.pricebar > button")
product_add.click()
time.sleep(2)

product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(4) > div.pricebar > button")
product_add.click()
time.sleep(2)

product_add = driver.find_element(By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(2) > div.pricebar > button")
product_add.click()
time.sleep(2)

shopping_cart = driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container > a > svg")
shopping_cart.click()
time.sleep(2)

shopping_detail_remove = driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_list > div:nth-child(4) > div.cart_item_label > div.item_pricebar > button")
shopping_detail_remove.click()
time.sleep(2)

checkout = driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button")
checkout.click()
time.sleep(2)

cancel_checkout = driver.find_element(By.CSS_SELECTOR, "#checkout_info_container > div > form > div.checkout_buttons > a")
cancel_checkout.click()

checkout = driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button")
checkout.click()

# Send Information 
first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("Salsa")

last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("Khairina")

postal_code = driver.find_element(By.ID, "postal-code")
postal_code.send_keys("56768")

continue_checkout = driver.find_element(By.CSS_SELECTOR, "#checkout_info_container > div > form > div.checkout_buttons > input")
continue_checkout.click()

input("tekan enter untuk keluar...")

# Tunggu beberapa detik lalu tutup browser
driver.quit()
