import ast

import pytest

from pageObject.openBrowser import OpenBrowser
from pageObject.register import Register
from utilites.datareader import Data


class Test_001_register:
    td = Data()
    testdata = td.data()
    reg = ast.literal_eval(testdata['DATA']['registration_data'])

    @pytest.mark.order(1)
    def test_registration(self, driver, config, locator, email):
        open_url = OpenBrowser(driver, config)
        register = Register(driver, locator)
        open_url.open_webBrowser()
        register.registration(email, self.reg)
        assert register.x == "nopCommerce demo store. Register"
