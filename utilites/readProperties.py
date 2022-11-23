import configparser

config = configparser.RawConfigParser()
config.read("../configurations/config.ini")


class Readconfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url
