import requests

class HttpManager:

    @staticmethod
    def post(url, data):
        result = requests.post(url, params=data)
        return result


