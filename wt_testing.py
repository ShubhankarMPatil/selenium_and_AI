from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv

# Set up Chrome options (can be modified to use headless mode, etc.)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode

# Initialize the driver
driver = webdriver.Chrome()

# Function to check element presence
def check_element_presence(by_type, value):
    try:
        element = driver.find_element(by_type, value)
        # print(f"Test Passed: Element found - {value}")
        return element
    except Exception as e:
        # print(f"Test Failed: Element not found - {value}")
        return None

def update_file(csv_file, case_id, result, status):
    rows = []

    # Read the CSV and update the Status for the specified Case ID
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[3] == row[4] and status == 1:  # Assuming "Case ID" is in the first column
                row[-1] = result   # Assuming "Status" is the last column
            elif row[4] == "undefined" and status == 0:
                row[-1] = result
            rows.append(row)

            row[5] = row[3]
    
    # Write back the updated rows
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write the header
        writer.writerows(rows)

count = 0

data = list(csv.reader(open("test_cases.csv")))

for i in range(1, len(data)):
    # Navigate to Amazon.in
    driver.get("E:\Study\selenium\WT-master\WT-master\FrontEnd\index.html")
    # Test 1: Check for the search bar
    username_input = check_element_presence(By.ID, "usernameInput")
    getData_button = check_element_presence(By.ID, "submitButton")

    # Fill in a test email or phone number
    if username_input:
        username_input.send_keys(data[i][3])  # Use a placeholder email

    # Click the Sign-In button to go to the login page
    if getData_button:
        getData_button.click()
        time.sleep(2)  # Wait for the login page to load

    usernameElement = check_element_presence(By.ID, "username_element")

    testCase = f"<strong>Username:</strong> {data[i][3]}"
    errorCase = f"<strong>Username:</strong> undefined"

    #print(usernameElement.get_attribute('innerHTML'))

    if usernameElement.get_attribute('innerHTML') == testCase:
        print(True)
        update_file("test_cases.csv", data[i][6], "1", 1)
        count += 1
    elif usernameElement.get_attribute('innerHTML') == errorCase:
        print(True)
        update_file("test_cases.csv", data[i][6], "1", 1)
        count += 1
    else:
        print(False)
        update_file("test_cases.csv", data[i][6], "0", 0)

if count == len(data):
    print("Website works as expected")
else:
    print(f"{count} test cases passed out of {len(data) - 1}")


# Close the browser
driver.quit()
