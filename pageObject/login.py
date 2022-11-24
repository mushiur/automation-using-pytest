import locators
import testData.logInData


class Login:

    def __init__(self, driver):
        self.driver = driver

    def log_in(self):
        self.driver.find_element("xpath", locators.log_in).click()
        self.driver.find_element("id", locators.email).send_keys(testData.logInData.loginEmail)
        self.driver.find_element("id", locators.password_field).send_keys(testData.logInData.loginPassword)
        self.driver.find_element("xpath", locators.confirm_log).click()
