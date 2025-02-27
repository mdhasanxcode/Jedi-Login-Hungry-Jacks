import os
import time
import random
import undetected_chromedriver as uc  # Using undetected-chromedriver

def login_with_selenium():
    # Set up Chrome options using undetected-chromedriver
    options = uc.ChromeOptions()
    
    # Set a realistic user agent
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    options.add_argument(f'user-agent={user_agent}')
    
    # Set a realistic window size
    options.add_argument("window-size=1920,1080")
    
    # Headless mode is commented out to reduce reCAPTCHA triggers
    # options.add_argument("--headless=new")
    
    # Optionally, add flags to further reduce detection
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Launch the browser using undetected-chromedriver
    driver = uc.Chrome(options=options)
    
    # Open the login page
    driver.get("https://jedi.hungryjacks.com.au/login")
    time.sleep(random.uniform(3, 5))  # Random delay to mimic human waiting
    
    # Update selectors as needed based on the actual page
    username_input = driver.find_element("id", "username")
    password_input = driver.find_element("id", "password")
    
    # Retrieve credentials from environment variables
    username = os.getenv("MYUSERNAME")
    password = os.getenv("MYPASSWORD")
    
    if username and password:
        print("Credentials found.")
    else:
        print("Missing credentials!")
    
    # Simulate human typing with random delays
    time.sleep(random.uniform(1, 2))
    username_input.send_keys(username)
    time.sleep(random.uniform(1, 2))
    password_input.send_keys(password)
    
    # Locate and click the login button with a delay
    login_button = driver.find_element("id", "login")
    time.sleep(random.uniform(1, 2))
    login_button.click()
    
    print("Login clicked. Waiting for the login process to complete...")
    time.sleep(random.uniform(3, 5))  # Wait for login to process
    
    # Log the current URL to verify navigation after login
    print(f"Current URL after login: {driver.current_url}")
    
    # Save the screenshot and page source after login
    driver.save_screenshot("after_login.png")
    with open("after_login.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    
    if "dashboard" in driver.current_url:
        print("Login successful!")
    else:
        print("Login failed!")
    
    driver.quit()

if __name__ == '__main__':
    login_with_selenium()