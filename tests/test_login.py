import pytest

from pageObject.login import Login
from utilites.readProperties import Readconfig


@pytest.mark.order(2)
class Test_002_LogIN:
    baseURL = Readconfig.getApplicationURL()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.log_in()
        self.lp.log_email()
        self.lp.log_password()
        self.lp.log_confirm()
        self.driver.close()
