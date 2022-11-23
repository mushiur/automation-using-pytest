import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pageObject.register import Register
from utilites.readProperties import Readconfig


@pytest.mark.order(2)
class Test_001_register:
    baseURL = Readconfig.getApplicationURL()

    def test_openPage(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.close()

    def test_registration(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.rp = Register(self.driver)
        self.rp.registration()
        self.rp.gender()
        self.rp.gender()
        self.rp.name()
        self.rp.dob()
        self.rp.email()
        self.rp.company()
        self.rp.password()
        self.rp.confirmPass()
        self.rp.regConfirm()
        self.rp.Logout()
        self.driver.close()
