import time

import locators
import testData.checkoutData


class CheckOut:
    def __init__(self, driver):
        self.driver = driver

    def checkout_button(self):
        self.driver.find_element("xpath", locators.term_condition_box).click()
        self.driver.find_element("xpath", locators.checkout_field).click()

    def billing_page(self):
        country = self.driver.find_element("xpath", locators.country_field)
        country.click()
        country.send_keys(testData.checkoutData.country)

        city = self.driver.find_element("xpath", locators.city_field)
        city.click()
        city.send_keys(testData.checkoutData.city)

        address_1 = self.driver.find_element("xpath", locators.address_1_field)
        address_1.click()
        address_1.send_keys(testData.checkoutData.Address1)

        pos_code = self.driver.find_element("xpath", locators.postal_field)
        pos_code.click()
        pos_code.send_keys(testData.checkoutData.pos_code)

        phn = self.driver.find_element("xpath", locators.phone_field)
        phn.click()
        phn.send_keys(testData.checkoutData.phn_num)

        cntnue = self.driver.find_element("xpath", locators.continue_button)
        cntnue.click()

    def checkout_page(self):
        self.driver.find_element("xpath", locators.shipping_method_field).click()
        self.driver.find_element("xpath", locators.payment_method_field).click()
        self.driver.find_element("xpath", locators.payment_info_field).click()
        self.driver.find_element("xpath", locators.confirm_order_filed).click()
        time.sleep(2)
        self.driver.find_element("xpath", locators.order_complete_field).click()
        time.sleep(2)
        self.driver.close()
