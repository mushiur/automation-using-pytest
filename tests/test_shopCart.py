import pytest
from pageObject.login import Login
from pageObject.search import Search
from pageObject.shoppingCart import ShoppingCart
from pageObject.openBrowser import OpenBrowser


class Test_004_shopCart:

    @pytest.mark.order(4)
    def test_shop(self, driver, config, locator, email):
        open_url = OpenBrowser(driver)
        login = Login(driver, locator)
        search = Search(driver, locator)
        shop_cart = ShoppingCart(driver, locator)
        open_url.open_webBrowser(config)
        login.log_in(email)
        search.search_box()
        shop_cart.shopping_cart()
