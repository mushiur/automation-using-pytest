import random


class ShoppingCart:
    def __init__(self, driver, locator):
        self.shopCart = None
        self.custom = None
        self.driver = driver
        self.cart_text_fieldBtn = locator["LOCATORS"]["cart_text_field"]
        self.add_cart_fieldBtn = locator["LOCATORS"]["add_cart_field"]
        self.shopping_cart_fieldBtn = locator["LOCATORS"]["shopping_cart_field"]

    def shopping_cart(self):
        element = self.driver.find_element("xpath", self.cart_text_fieldBtn)
        element.click()
        self.custom = self.driver.title
        element.send_keys(random.randint(0, 9))
        self.driver.find_element("id", self.add_cart_fieldBtn).click()
        self.driver.find_element("xpath", self.shopping_cart_fieldBtn).click()
        self.shopCart = self.driver.title
