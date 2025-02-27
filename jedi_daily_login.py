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
    username = os.getenv("MYUSERNAME")
    password = os.getenv("MYPASSWORD")
    
    print("Credentials from the environment achived")
    
    username_input.send_keys(username)
    password_input.send_keys(password)
    
    if username and password:
        print("Credentials found.")
    else:
        print("Missing credentials!")
    
    print("Credentials sent successfully")
    
    login_button = driver.find_element("id", "login")
    login_button.click()
    
    print("login clicked. Program waiting for 3 sec.")
    time.sleep(3)  # Wait for login to process
    
    #Url after login
    print(f"After 3 sec.\nCurrent Url:{driver.current_url}")
    
    # Save screenshotafter login
    driver.save_screenshot("after_login.png")
    
    # Save Webpage after login
    with open("after_login.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    
    if "dashboard" in driver.current_url:
        print("Login successful!")
    else:
        print("Login failed!")
    
    driver.quit()

if __name__ == '__main__':
    login_with_selenium()