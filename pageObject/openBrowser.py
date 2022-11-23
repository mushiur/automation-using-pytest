from utilites.readProperties import Readconfig


class OpenBrowser:

    def __init__(self, driver):
        self.driver = driver

    def open_webBrowser(self, config):
        # s = Service("../Driver/chromedriver.exe")
        # self.driver = webdriver.Chrome(service=s)
        baseURL = Readconfig.getApplicationURL(config)
        self.driver.get(baseURL)
        self.driver.implicitly_wait(20)
