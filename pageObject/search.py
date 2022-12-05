
class Search:
    def __init__(self, driver, locator):
        self.search = None
        self.driver = driver
        self.search_fieldBtn = locator["LOCATORS"]["search_field"]
        self.choose_productBtn = locator["LOCATORS"]["choose_product"]

    def search_box(self, search):
        element = self.driver.find_element("id", self.search_fieldBtn)
        element.click()
        element.send_keys(search['productName'])
        element.submit()
        self.search = self.driver.title
        self.driver.find_element("xpath", self.choose_productBtn).click()
        

