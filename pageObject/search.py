import locators
import testData.searchData


class Search:
    def __init__(self, driver):
        self.driver = driver

    def search_box(self):
        element = self.driver.find_element("id", locators.search_field)
        element.click()
        element.send_keys(testData.searchData.productName)
        element.submit()
        self.driver.find_element("xpath", locators.choose_product).click()

