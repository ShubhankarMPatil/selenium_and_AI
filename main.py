from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Set up Chrome options (can be modified to use headless mode, etc.)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode

# Initialize the driver
driver = webdriver.Chrome()

# Navigate to Amazon.in
driver.get("https://www.amazon.in")

# Function to check element presence
def check_element_presence(by_type, value):
    try:
        element = driver.find_element(by_type, value)
        print(f"Test Passed: Element found - {value}")
        return element
    except Exception as e:
        print(f"Test Failed: Element not found - {value}")
        return None

# Test 1: Check for the search bar
check_element_presence(By.ID, "twotabsearchtextbox")

# Test 2: Check for the Amazon logo
check_element_presence(By.XPATH, "//a[@aria-label='Amazon.in']")

# Test 3: Check for the cart icon
check_element_presence(By.ID, "nav-cart")

# Test 4: Check for the sign-in button
sign_in_button = check_element_presence(By.ID, "nav-link-accountList")

# Click the Sign-In button to go to the login page
if sign_in_button:
    sign_in_button.click()
    time.sleep(2)  # Wait for the login page to load

# Test 5: Check for the email/phone number field on the login page
email_field = check_element_presence(By.ID, "ap_email")

# Fill in a test email or phone number
if email_field:
    email_field.send_keys("test_email@example.com")  # Use a placeholder email
    email_field.send_keys(Keys.RETURN)  # Press enter to proceed

    time.sleep(2)  # Wait for the next page to load (password entry)

# Test 6: Check for the password field
password_field = check_element_presence(By.ID, "ap_password")

# Simulate filling in the password field
if password_field:
    password_field.send_keys("dummy_password")  # Use a placeholder password

# Test 7: Check for the "Sign-In" button and click it (simulate login)
sign_in_submit = check_element_presence(By.ID, "signInSubmit")

if sign_in_submit:
    # Simulate clicking the sign-in button
    print("Attempting login (placeholder email and password used)...")
    sign_in_submit.click()

    # Wait for a few seconds to simulate a login attempt
    time.sleep(3)

# Close the browser
driver.quit()
