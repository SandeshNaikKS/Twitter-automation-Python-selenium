# Twitter Bot Using Selenium

This bot automates the following tasks on Twitter:
1. Logs into your Twitter account.
2. Follows a list of specified users.
3. Likes a specific tweet.

---

## Prerequisites

### Software Requirements
1. **Python** (3.7 or later)
2. **Google Chrome** (latest version)
3. **ChromeDriver** (compatible with your Chrome version)

### Python Packages
Install the required Python libraries by running:
```bash
pip install selenium
```

---

## Configuration

### Twitter Credentials
Update the following variables in the script with your Twitter login credentials:
```python
EMAIL = "YourTwitterEmailOrUsername"
PASSWORD = "YourTwitterPassword"
```

### Users to Follow
List the usernames of the accounts you wish to follow:
```python
USERS_TO_FOLLOW = ["User1", "User2"]
```

### Tweet to Like
Set the URL of the tweet you want to like:
```python
TWEET_URL = "https://twitter.com/User/status/TweetID"
```

### ChromeDriver Path
Specify the path to your `chromedriver.exe` file:
```python
chrome_driver_path = "C:/path/to/chromedriver.exe"
```

---

## How to Run the Script

1. **Download ChromeDriver**  
   Download the appropriate ChromeDriver version for your Chrome browser from the official [ChromeDriver website](https://chromedriver.chromium.org/downloads).

2. **Configure the Script**  
   Update the placeholders in the script with your details as described in the configuration section.

3. **Run the Script**  
   Execute the script using Python:
   ```bash
   python twitter_bot.py
   ```

---

## Bot Workflow

1. **Login**:  
   The bot navigates to the Twitter login page and logs in using the provided credentials.

2. **Follow Users**:  
   For each user in the `USERS_TO_FOLLOW` list, the bot navigates to their profile and clicks the **Follow** button.

3. **Like a Tweet**:  
   The bot opens the specified tweet URL and clicks the **Like** button.

4. **Exit**:  
   The bot closes the browser once all tasks are completed.

---

## Troubleshooting

1. **ChromeDriver Compatibility**:  
   Ensure the ChromeDriver version matches your Chrome browser version.

2. **Twitter Layout Changes**:  
   If the script fails to find elements (e.g., follow or like buttons), Twitter's layout may have changed. Update the XPaths in the script accordingly.

3. **Login Issues**:  
   - If Twitter requests additional verification, the script may need to be updated to handle it.
   - Make sure your credentials are correct.

4. **Rate Limits**:  
   Twitter may enforce rate limits or temporary bans for excessive activity. Use the bot responsibly.
