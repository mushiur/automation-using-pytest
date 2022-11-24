import pytest
from pageObject.login import Login
from pageObject.search import Search
from pageObject.shoppingCart import ShoppingCart
from pageObject.checkout import CheckOut
from pageObject.openBrowser import OpenBrowser


class Test_005_checkout:
    @pytest.mark.order(5)
    def test_checkout(self, driver, config):
        open_url = OpenBrowser(driver)
        login = Login(driver)
        search = Search(driver)
        shop_cart = ShoppingCart(driver)
        check_out = CheckOut(driver)
        open_url.open_webBrowser(config)
        login.log_in()
        search.search_box()
        shop_cart.shopping_cart()
        check_out.checkout_billing_details()
