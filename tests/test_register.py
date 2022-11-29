import pytest

from pageObject.openBrowser import OpenBrowser
from pageObject.register import Register


class Test_001_register:

    @pytest.mark.order(1)
    def test_registration(self, driver, config, locator, email):
        open_url = OpenBrowser(driver, config)
        register = Register(driver, locator)
        open_url.open_webBrowser()
        register.registration()
        register.gender()
        register.gender()
        register.name()
        register.dob()
        register.email(email)
        register.company()
        register.password()
        register.confirmPass()
        register.regConfirm()
        register.logout()
