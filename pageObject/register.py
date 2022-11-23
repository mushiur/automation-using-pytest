import testData.registerData
import locators
from utilites.readProperties import Readconfig


class Register:

    def __init__(self, driver):
        self.driver = driver

    def registration(self):
        self.driver.find_element("xpath", locators.registration).click()

    def gender(self):
        self.driver.find_element("xpath", locators.gender).click()

    def name(self):
        # imported from testdata file
        self.driver.find_element("id", locators.first_name).send_keys(testData.registerData.firstName)
        self.driver.find_element("id", locators.last_name ).send_keys(testData.registerData.lastName)

    def dob(self):
        # imported from testdata file
        self.driver.find_element("name", locators.birth_day).send_keys(testData.registerData.date)
        self.driver.find_element("name", locators.birth_month).send_keys(testData.registerData.month)
        self.driver.find_element("name", locators.birth_year).send_keys(testData.registerData.year)

    def email(self):
        self.driver.find_element("id", locators.email).send_keys(testData.registerData.email)

    def company(self):
        self.driver.find_element("id", locators.company_box).send_keys(testData.registerData.company)

    def password(self):
        self.driver.find_element("id", locators.password_field).send_keys(testData.registerData.password)

    def confirmPass(self):
        self.driver.find_element("id", locators.confirm_pass_field).send_keys(testData.registerData.password)

    def regConfirm(self):
        self.driver.find_element("xpath", locators.reg_confirm_field).click()

    def Logout(self):
        self.driver.find_element("xpath", locators.log_out).click()
