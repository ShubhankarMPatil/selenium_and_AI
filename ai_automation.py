import cv2
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.action_builder import ActionBuilder
import time

# Path to ChromeDriver
driver = webdriver.Chrome()

# Load the website you want to test
driver.get("E:\Study\selenium\WT-master\WT-master\FrontEnd\index.html")  # Use double backslashes
time.sleep(3)  # Wait for the page to fully load

def check_element_presence(by_type, value):
    try:
        element = driver.find_element(by_type, value)
        # print(f"Test Passed: Element found - {value}")
        return element
    except Exception as e:
        # print(f"Test Failed: Element not found - {value}")
        return None

# Function to find element using OpenCV and return its position
def find_element_by_image(reference_image_path):
    # Capture screenshot of the current browser window
    screenshot = 'page_screenshot.png'
    driver.save_screenshot(screenshot)

    # Read both the screenshot and reference element images
    img = cv2.imread(screenshot)
    reference_img = cv2.imread(reference_image_path)

    # Use template matching to find the location of the element
    result = cv2.matchTemplate(img, reference_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Define a threshold to consider it a match
    threshold = 0.8
    if max_val >= threshold:
        top_left = max_loc
        h, w, _ = reference_img.shape
        # Calculate the center point of the element
        center_x = top_left[0] + (h // 2)
        center_y = top_left[1] + (w // 2)
        return center_x, center_y
    else:
        print("Element not found on the page.")
        return None, None

# Function to click on an element using Selenium
def click_at_position(x, y):
    if x is not None and y is not None:
        # Move to the location using Selenium's ActionChains
        element = driver.find_element(By.TAG_NAME, 'body')  # Get the body as a reference element
        actions = ActionChains(driver)
        
        # Move to the element's center point and perform a click
        actions.move_to_element_with_offset(element, x, y).click().perform()
        print(f"Clicked on the element at ({x}, {y})")
    else:
        print("Unable to click; no valid coordinates.")

# Example usage to find and click on elements
actions = ActionChains(driver)
x, y = find_element_by_image("wt_search.png")
click_at_position(x, y)
username = check_element_presence(By.ID, "usernameInput")
username.send_keys("MeetMavani")
x, y = find_element_by_image("wt_getdata.png")  # Find the target UI element
click_at_position(x, y)  # Simulate click using Selenium
submit = check_element_presence(By.ID, "submitButton")
submit.click()
time.sleep(10)

# Close the browser after testing
driver.quit()
