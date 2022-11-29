import pytest

from pageObject.openBrowser import OpenBrowser
from pageObject.register import Register


class Test_001_register:

    @pytest.mark.order(1)
    def test_registration(self, driver, config, locator):
        open_url = OpenBrowser(driver)
        register = Register(driver, locator)
        open_url.open_webBrowser(config)
        register.registration()
        register.gender()
        register.gender()
        register.name()
        register.dob()
        register.email()
        register.company()
        register.password()
        register.confirmPass()
        register.regConfirm()
        register.logout()
