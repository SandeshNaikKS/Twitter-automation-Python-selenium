from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace these with your Twitter credentials
EMAIL = "Jaanu2909"
PASSWORD = "pallavilovestharu"

# List of users you want to follow
USERS_TO_FOLLOW = ["TheNameIsYash", "PuneethRajkumar"]

# URL of the tweet you want to like
TWEET_URL = "https://x.com/PuneethRajkumar/status/1453338815603478532/photo/1"  # Replace with actual tweet URL

# Path to the ChromeDriver executable
chrome_driver_path = "C:/Users/ADMIN/Downloads/chromedriver-win64/chromedriver.exe"

# Setup the WebDriver (using Chrome in this example)
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open Twitter login page
driver.get("https://twitter.com/login")
time.sleep(5)  # Wait for the page to load

# Log in to Twitter
email_input = driver.find_element(By.NAME, "text")
email_input.send_keys(EMAIL)
email_input.send_keys(Keys.RETURN)
time.sleep(5)  # Wait for next page

password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)
time.sleep(5)  # Wait for login to complete

# Follow each user in the list
for user in USERS_TO_FOLLOW:
    driver.get(f"https://twitter.com/{user}")
    time.sleep(5)  # Wait for the page to load
    
    try:
        # Try to find and click the follow button
        follow_button = driver.find_element(By.XPATH, '//span[text()="Follow"]')
        follow_button.click()
        time.sleep(5)  # Wait for the follow action
    except Exception as e:
        print(f"Could not follow {user}. Reason: {e}")

# Like a specific tweet
driver.get(TWEET_URL)
time.sleep(5)  # Wait for the page to load

try:
    # Locate and click the Like button using the provided XPath
    like_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div[1]/div[2]/div/div/div/div[3]/button')
    like_button.click()
    time.sleep(2)  # Wait for the like action
except Exception as e:
    print(f"Could not like the tweet. Reason: {e}")

# Close the browser
driver.quit()
