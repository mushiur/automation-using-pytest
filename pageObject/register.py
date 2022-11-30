import testData.registerData


class Register:

    def __init__(self, driver, locator):
        self.driver = driver
        self.regBtn = locator["LOCATORS"]["registration"]
        self.genderBtn = locator["LOCATORS"]["gender"]
        self.firstnameBtn = locator["LOCATORS"]["first_name"]
        self.lastnameBtn = locator["LOCATORS"]["last_name"]
        self.birthdayBtn = locator["LOCATORS"]["birth_day"]
        self.birth_monthBtn = locator["LOCATORS"]["birth_month"]
        self.birth_yearBtn = locator["LOCATORS"]["birth_year"]
        self.emailBtn = locator["LOCATORS"]["email"]
        self.company_boxBtn = locator["LOCATORS"]["company_box"]
        self.password_fieldBtn = locator["LOCATORS"]["password_field"]
        self.confirm_pass_fieldBtn = locator["LOCATORS"]["confirm_pass_field"]
        self.reg_confirm_fieldBtn = locator["LOCATORS"]["reg_confirm_field"]
        self.log_outBtn = locator["LOCATORS"]["log_out"]

    def registration(self, email, reg):
        self.driver.find_element("xpath", self.regBtn).click()
        self.driver.find_element("xpath", self.genderBtn).click()
        # imported from testdata file
        self.driver.find_element("id", self.firstnameBtn).send_keys(reg['firstName'])
        self.driver.find_element("id", self.lastnameBtn).send_keys(reg['lastName'])
        # imported from testdata file
        self.driver.find_element("name", self.birthdayBtn).send_keys(reg['date'])
        self.driver.find_element("name", self.birth_monthBtn).send_keys(reg['month'])
        self.driver.find_element("name", self.birth_yearBtn).send_keys(reg['year'])
        self.driver.find_element("id", self.emailBtn).send_keys(email)
        self.driver.find_element("id", self.company_boxBtn).send_keys(reg['company'])
        self.driver.find_element("id", self.password_fieldBtn).send_keys(reg['password'])
        self.driver.find_element("id", self.confirm_pass_fieldBtn).send_keys(reg['password'])
        self.driver.find_element("xpath", self.reg_confirm_fieldBtn).click()
        self.driver.find_element("xpath", self.log_outBtn).click()
