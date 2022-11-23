from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class OpenBrowser:

    def __init__(self, driver):
        self.driver = driver

    def open_webBrowser(self):
        # s = Service("../Driver/chromedriver.exe")
        # self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
