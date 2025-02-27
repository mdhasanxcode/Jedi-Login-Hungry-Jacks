import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def login_with_selenium():
    options = Options()
    options.add_argument("--headless=new")  # Runs without a visible browser window
    driver = webdriver.Chrome(options=options)
    
    driver.get("https://jedi.hungryjacks.com.au/login")
    time.sleep(3)  # Wait for the page to load
    
    # Update the selectors based on the actual page elements.
    username_input = driver.find_element("id", "username")
    password_input = driver.find_element("id", "password")
    
    # Get credentials from environment variables
    username = "MdRakibHasan"
    password = "123456"
    
    username_input.send_keys(username)
    password_input.send_keys(password)
    # Get credentials from environment variables
    username = os.getenv("MYUSERNAME")
    password = os.getenv("MYPASSWORD")
    
    username_input.send_keys(username)
    password_input.send_keys(password)
    
    login_button = driver.find_element("id", "login")
    login_button.click()
    
    time.sleep(3)  # Wait for login to process
    
    if "dashboard" in driver.current_url:
        print("Login successful!")
    else:
        print("Login failed!")
    
    driver.quit()

if __name__ == '__main__':
    login_with_selenium()
