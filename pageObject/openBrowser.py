
class OpenBrowser:

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config["common info"]["baseURL"]

    def open_webBrowser(self):
        baseURL = self.config
        self.driver.get(baseURL)
        self.driver.implicitly_wait(20)
