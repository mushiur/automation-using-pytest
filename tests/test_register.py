import pytest

from pageObject.openBrowser import OpenBrowser
from pageObject.register import Register


class Test_001_register:

    # def test_openPage(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()
    #     self.driver.close()

    @pytest.mark.order(1)
    def test_registration(self, driver, config):
        open_url = OpenBrowser(driver)
        register = Register(driver)
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
