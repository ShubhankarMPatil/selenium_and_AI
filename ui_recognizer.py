import time
import cv2
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from io import BytesIO
from PIL import Image

# Load the DeepUI model (pseudo-code, replace with actual model loading)
def load_deepui_model():
    # Load the model here
    model = "deepui_model"  # Replace this with actual model loading
    return model

# Function to find a specific UI element by name
def find_ui_element_by_name(image_np, element_name, model):
    # Use the DeepUI model to detect elements in the image
    detected_elements = model.detect_elements(image_np)  # Pseudo-function

    # Check if the element name exists in detected elements
    for element in detected_elements:
        if element['name'] == element_name:
            return element['position']  # Return position (x, y, width, height)

    return None

# Function to take a screenshot and find the UI element
def search_and_click_element(url, element_name):
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome()

    try:
        # Open the webpage
        driver.get(url)
        time.sleep(2)  # Wait for the page to load

        # Take a screenshot
        screenshot = driver.get_screenshot_as_png()
        image = Image.open(BytesIO(screenshot))
        image_np = np.array(image)

        # Load the DeepUI model
        model = load_deepui_model()

        # Find the UI element
        element_position = find_ui_element_by_name(image_np, element_name, model)

        if element_position:
            x, y, w, h = element_position  # Assuming position is returned as (x, y, width, height)
            center_x = x + w // 2
            center_y = y + h // 2

            # Click on the element
            webdriver.ActionChains(driver).move_to_element_with_offset(driver.find_element(By.TAG_NAME, 'body'), center_x, center_y).click().perform()

            print("Yes")  # Element found and clicked
        else:
            print("No")  # Element not found
    finally:
        driver.quit()

# Example usage
search_and_click_element('https://www.amazon.in', 'search bar')  # Replace with the actual URL and element name
