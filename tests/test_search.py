import pytest
from pageObject.search import Search
from pageObject.login import Login
from pageObject.openBrowser import OpenBrowser


class Test_003_search:
    @pytest.mark.order(3)
    def test_search(self, driver, config, locator, email):
        open_url = OpenBrowser(driver)
        login = Login(driver, locator)
        search = Search(driver, locator)
        open_url.open_webBrowser(config)
        login.log_in(email)
        search.search_box()

