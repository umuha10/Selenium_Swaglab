from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
username_field = driver.find_element(By.ID, "user-name").send_keys("umu")
password_field = driver.find_element(By.ID, "password").send_keys("habibah")
login_button = driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Login (Negative Case #2)
driver.refresh()
username_field = driver.find_element(By.ID, "user-name").send_keys("umu")
password_field = driver.find_element(By.ID, "password").send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Login (Negative Case #3)
driver.refresh()
username_field = driver.find_element(By.ID, "user-name").send_keys("standard_user")
password_field = driver.find_element(By.ID, "password").send_keys("123")
login_button = driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Login (Negative Case #4)
driver.refresh()
username_field = driver.find_element(By.ID, "user-name").send_keys("")
password_field = driver.find_element(By.ID, "password").send_keys("")
login_button = driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Login (Possitive Case #5)
driver.refresh
username_field = driver.find_element(By.ID, "user-name").send_keys("standard_user")
password_field = driver.find_element(By.ID, "password").send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button").click()

# ------------------------
# | VERIFY BUTTON BURGER |
# ------------------------

# Button link All Item (Positive case #6)
burger_button = driver.find_element(By.CLASS_NAME, "bm-burger-button").click()

# Button link All item (Possitive case #7)
wait = WebDriverWait(driver, 10)
all_item = wait.until(EC.element_to_be_clickable((By.ID, "inventory_sidebar_link"))).click()

# Button link All item (Possitive case #8)
burger_button = driver.find_element(By.CLASS_NAME, "bm-burger-button").click()
wait = WebDriverWait(driver, 10)
about_button = wait.until(EC.element_to_be_clickable((By.ID, "about_sidebar_link"))).click()
driver.back()
time.sleep(2)

# Button icon close (Possitive case #9)
close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bm-cross-button"))).click()

# Button logout (Possitive case #10)
burger_button = driver.find_element(By.CLASS_NAME, "bm-burger-button").click()
logout_button = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()


input("tekan enter untuk keluar...")

# Tunggu beberapa detik lalu tutup browser
driver.quit()
