import time

import testData.checkoutData


class CheckOut:
    def __init__(self, driver, locator):
        self.driver = driver
        self.shop_cartBtn = locator["LOCATORS"]["shop_cart"]
        self.term_condition_boxBtn = locator["LOCATORS"]["term_condition_box"]
        self.checkout_fieldBtn = locator["LOCATORS"]["checkout_field"]
        self.country_fieldBtn = locator["LOCATORS"]["country_field"]
        self.city_fieldBtn = locator["LOCATORS"]["city_field"]
        self.address_1_fieldBtn = locator["LOCATORS"]["address_1_field"]
        self.postal_fieldBtn = locator["LOCATORS"]["postal_field"]
        self.phone_field = locator["LOCATORS"]["phone_field"]
        self.continue_button = locator["LOCATORS"]["continue_button"]
        self.shipping_method_field = locator["LOCATORS"]["shipping_method_field"]
        self.payment_method_field = locator["LOCATORS"]["payment_method_field"]
        self.payment_info_field = locator["LOCATORS"]["payment_info_field"]
        self.confirm_order_filed = locator["LOCATORS"]["confirm_order_filed"]
        self.order_complete_field = locator["LOCATORS"]["order_complete_field"]

    def checkout_billing_details(self):
        self.driver.find_element("xpath", self.shop_cartBtn).click()
        self.driver.find_element("xpath", self.term_condition_boxBtn).click()
        self.driver.find_element("xpath", self.checkout_fieldBtn).click()

        country = self.driver.find_element("xpath", self.country_fieldBtn)
        country.click()
        country.send_keys(testData.checkoutData.country)

        city = self.driver.find_element("xpath", self.city_fieldBtn)
        city.click()
        city.send_keys(testData.checkoutData.city)

        address_1 = self.driver.find_element("xpath", self.address_1_fieldBtn)
        address_1.click()
        address_1.send_keys(testData.checkoutData.Address1)

        pos_code = self.driver.find_element("xpath", self.postal_fieldBtn)
        pos_code.click()
        pos_code.send_keys(testData.checkoutData.pos_code)

        phn = self.driver.find_element("xpath", self.phone_field)
        phn.click()
        phn.send_keys(testData.checkoutData.phn_num)

        cntnue = self.driver.find_element("xpath", self.continue_button)
        cntnue.click()

        self.driver.find_element("xpath", self.shipping_method_field).click()
        self.driver.find_element("xpath", self.payment_method_field).click()
        self.driver.find_element("xpath", self.payment_info_field).click()
        self.driver.find_element("xpath", self.confirm_order_filed).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.order_complete_field).click()
        time.sleep(2)
