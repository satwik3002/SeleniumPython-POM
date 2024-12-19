from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.username_field = (By.ID, 'username')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.XPATH, "/html/body/main/section/div/div/div/form/div[2]/button")

    def get_email_field(self):
        return self.driver.find_element(self.username_field)

    def get_password_field(self):
        return self.driver.find_element(self.password_field)

    def get_login_button(self):
        return self.driver.find_element(self.login_button)

    def enter_email(self, email):
        self.get_email_field().send_keys(email)

    def enter_password(self, password):
        self.get_password_field().send_keys(password)

    def click_login(self):
        self.get_login_button().click()


    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()


