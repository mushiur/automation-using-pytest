import testData.searchData


class Search:
    def __init__(self, driver, locator):
        self.driver = driver
        self.search_fieldBtn = locator["LOCATORS"]["search_field"]
        self.choose_productBtn = locator["LOCATORS"]["choose_product"]

    def search_box(self):
        element = self.driver.find_element("id", self.search_fieldBtn)
        element.click()
        element.send_keys(testData.searchData.productName)
        element.submit()
        self.driver.find_element("xpath", self.choose_productBtn).click()

