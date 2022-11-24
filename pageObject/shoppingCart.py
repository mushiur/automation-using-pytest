import random

import locators


class ShoppingCart:
    def __init__(self, driver):
        self.driver = driver

    def shopping_cart(self):
        element = self.driver.find_element("xpath", locators.cart_text_field)
        element.click()
        element.send_keys(random.randint(0, 9))
        self.driver.find_element("id", locators.add_cart_field).click()
        self.driver.find_element("xpath", locators.shopping_cart_field).click()
