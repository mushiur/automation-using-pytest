import pytest
import ast
from pageObject.login import Login
from pageObject.checkout import CheckOut
from pageObject.openBrowser import OpenBrowser
from utilites.datareader import Data


class Test_005_checkout:
    td = Data()
    testData = td.data()
    log = ast.literal_eval(testData['DATA']['registration_data'])
    checkOut = ast.literal_eval(testData['DATA']['checkOut_data'])

    @pytest.mark.order(5)
    def test_checkout(self, driver, config, locator, email):
        open_url = OpenBrowser(driver, config)
        login = Login(driver, locator)
        check_out = CheckOut(driver, locator)
        open_url.open_webBrowser()
        login.log_in(email, self.log)
        check_out.checkout_billing_details(self.checkOut)
        assert check_out.shopCart == "nopCommerce demo store. Shopping Cart"
        assert check_out.checkOut_title == "nopCommerce demo store. Checkout"
        assert check_out.homeTitle == "nopCommerce demo store"
