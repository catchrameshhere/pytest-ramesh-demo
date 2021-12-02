from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.driver = driver

    """locators"""
    email = "email"
    passwd = "pass"

    def login_with_cred(self, username, password):
        self.driver.find_element(By.ID, self.email).send_keys(username)
        self.driver.find_element(By.ID, self.passwd).send_keys(password)
