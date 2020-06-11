import inspect
import logging
from api.httpmanager import HttpManager

logger = logging.getLogger("example." + __name__)

class PaytureClient:


    BASE_URL = "https://sandbox3.payture.com/api/"
    PAY_URL = BASE_URL + "Pay"
    BLOCK_URL = BASE_URL + "Block"



    @staticmethod
    def block(data):
        result = HttpManager.post(PaytureClient.BLOCK_URL, data)
        return result

    @staticmethod
    def pay(data):
        result = HttpManager.post(PaytureClient.PAY_URL, data)
        return result




