import time

from selenium import webdriver

from POM.Login_page import LoginPage


def test_validateLogin():
    baseURL = 'https://auth.hollandandbarrett.com/u/login'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseURL)

    # Optional: wait for the page to load completely (use WebDriverWait for better reliability)
    time.sleep(3)  # You can replace this with WebDriverWait if needed

    # Create an instance of Loginpage class
    lp = LoginPage(driver)

    # Call login method with email and password
    lp.login("satwikkatamaraju@gmail.com", "Y2#ssv@Xp/xP8Wt")

    #Wait for the page to load after login
    time.sleep(3)

    # Check if the title is as expected
    actual_title = driver.title
    expected_title = "Sign in - to your account, for the best experience"  # Corrected title string

    if actual_title == expected_title:
        print("Login Successful")
    else:
        print("Login Unsuccessful")

    # Close the browser
    driver.quit()


