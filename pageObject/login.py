import locators
import testData.logInData


class Login:

    def __init__(self, driver):
        self.driver = driver

    def log_in(self):
        self.driver.find_element("xpath", locators.log_in).click()

    def log_email(self):
        self.driver.find_element("id", locators.email).send_keys(testData.logInData.loginEmail)

    def log_password(self):
        self.driver.find_element("id", locators.password_field).send_keys(testData.logInData.loginPassword)

    def log_confirm(self):
        self.driver.find_element("xpath", locators.confirm_log).click()
