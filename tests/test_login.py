import pytest
import ast

from pageObject.login import Login
from pageObject.openBrowser import OpenBrowser
from utilites.datareader import Data


class Test_002_LogIN:
    td = Data()
    testData = td.data()
    log = ast.literal_eval(testData['DATA']['registration_data'])

    @pytest.mark.order(2)
    def test_login(self, driver, config, locator, email):
        open_url = OpenBrowser(driver, config)
        login = Login(driver, locator)
        open_url.open_webBrowser()
        login.log_in(email=email, log=self.log)
