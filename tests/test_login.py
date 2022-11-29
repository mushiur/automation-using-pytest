import pytest

from pageObject.login import Login
from pageObject.openBrowser import OpenBrowser


class Test_002_LogIN:

    @pytest.mark.order(2)
    def test_login(self, driver, config, locator, email):
        open_url = OpenBrowser(driver,config)
        login = Login(driver, locator)
        open_url.open_webBrowser()
        login.log_in(email)

