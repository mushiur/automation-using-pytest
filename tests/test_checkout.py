import pytest
from pageObject.login import Login
from pageObject.checkout import CheckOut
from pageObject.openBrowser import OpenBrowser


class Test_005_checkout:
    @pytest.mark.order(5)
    def test_checkout(self, driver, config, locator, email):
        open_url = OpenBrowser(driver, config)
        login = Login(driver, locator)
        check_out = CheckOut(driver, locator)
        open_url.open_webBrowser()
        login.log_in(email)
        check_out.checkout_billing_details()
