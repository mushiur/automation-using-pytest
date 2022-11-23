
class Readconfig:
    @staticmethod
    def getApplicationURL(config):
        url = config.get('common info', 'baseURL')
        return url
