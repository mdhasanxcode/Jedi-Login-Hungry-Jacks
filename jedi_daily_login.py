import os
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.options import Options
import time

def login_with_selenium():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--headless=new")  # Runs without a visible browser window
    
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    
    stealth(driver,
        languages=["en-US", "en"],
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
    
    
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
    
    time.sleep(5)
    # Save screenshotafter login
    driver.save_screenshot("before_login.png")
    time.sleep(5)
    
    login_button = driver.find_element("id", "login")
    login_button.click()
    
    print("login clicked. Program waiting for 3 sec.")
    time.sleep(4)  # Wait for login to process
    
    #Url after login
    print(f"After 3 sec.\nCurrent Url:{driver.current_url}")
    
    # Save screenshotafter login
    driver.save_screenshot("after_login.png")
    
    # Save Webpage after login
    # with open("after_login.html", "w", encoding="utf-8") as f:
    #     f.write(driver.page_source)
    
    if "dashboard" in driver.current_url:
        print("Login successful!")
    else:
        print("Login failed!")
    
    driver.quit()

if __name__ == '__main__':
    login_with_selenium()
