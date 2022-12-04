import pytest
import ast
from pageObject.login import Login
from pageObject.search import Search
from pageObject.shoppingCart import ShoppingCart
from pageObject.openBrowser import OpenBrowser
from utilites.datareader import Data


class Test_004_shopCart:
    td = Data()
    testData = td.data()
    log = ast.literal_eval(testData['DATA']['registration_data'])
    search = ast.literal_eval(testData['DATA']['search_data'])

    @pytest.mark.order(4)
    def test_shop(self, driver, config, locator, email):
        open_url = OpenBrowser(driver, config)
        login = Login(driver, locator)
        search = Search(driver, locator)
        shop_cart = ShoppingCart(driver, locator)
        open_url.open_webBrowser()
        login.log_in(email, self.log)
        search.search_box(self.search)
        shop_cart.shopping_cart()
