import testData.logInData


class Login:

    def __init__(self, driver, locator):
        self.driver = driver
        self.loginBtn = locator["LOCATORS"]["log_in"]
        self.email = locator["LOCATORS"]["email"]
        self.password_field = locator["LOCATORS"]["password_field"]
        self.conBtn = locator["LOCATORS"]["confirm_log"]

    def log_in(self):
        self.driver.find_element("xpath", self.loginBtn).click()
        self.driver.find_element("id", self.email).send_keys(testData.logInData.loginEmail)
        self.driver.find_element("id", self.password_field).send_keys(testData.logInData.loginPassword)
        self.driver.find_element("xpath", self.conBtn).click()
