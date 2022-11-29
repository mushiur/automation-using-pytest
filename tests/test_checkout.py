import pytest
from pageObject.login import Login
from pageObject.checkout import CheckOut
from pageObject.openBrowser import OpenBrowser


class Test_005_checkout:
    @pytest.mark.order(5)
    def test_checkout(self, driver, config, locator):
        open_url = OpenBrowser(driver)
        login = Login(driver, locator)
        check_out = CheckOut(driver, locator)
        open_url.open_webBrowser(config)
        login.log_in()
        check_out.checkout_billing_details()
