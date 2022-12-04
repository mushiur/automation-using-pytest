import testData.logInData


class Login:

    def __init__(self, driver, locator):
        self.x = None
        self.driver = driver
        self.loginBtn = locator["LOCATORS"]["log_in"]
        self.email = locator["LOCATORS"]["email"]
        self.password_field = locator["LOCATORS"]["password_field"]
        self.conBtn = locator["LOCATORS"]["confirm_log"]

    def log_in(self, email, log):
        self.driver.find_element("xpath", self.loginBtn).click()
        self.driver.find_element("id", self.email).send_keys(email)
        self.driver.find_element("id", self.password_field).send_keys(log['password'])
        self.driver.find_element("xpath", self.conBtn).click()
        self.x = self.driver.title
