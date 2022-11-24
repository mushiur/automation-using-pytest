import pytest
from pageObject.search import Search
from pageObject.login import Login
from pageObject.openBrowser import OpenBrowser


class Test_003_search:

    def test_search(self, driver, config):
        open_url = OpenBrowser(driver)
        login = Login(driver)
        search = Search(driver)
        open_url.open_webBrowser(config)
        login.log_in()
        search.search_box()
        search.choose_product()
