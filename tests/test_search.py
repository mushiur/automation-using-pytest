import pytest
import ast
from pageObject.search import Search
from pageObject.login import Login
from pageObject.openBrowser import OpenBrowser
from utilites.datareader import Data


class Test_003_search:
    td = Data()
    testData = td.data()
    log = ast.literal_eval(testData['DATA']['registration_data'])
    search = ast.literal_eval(testData['DATA']['search_data'])

    @pytest.mark.order(3)
    def test_search(self, driver, config, locator, email):
        open_url = OpenBrowser(driver, config)
        login = Login(driver, locator)
        search = Search(driver, locator)
        open_url.open_webBrowser()
        login.log_in(email, log=self.log)
        assert login.x == "nopCommerce demo store"
        search.search_box(self.search)
        assert search.search == "nopCommerce demo store. Search"
