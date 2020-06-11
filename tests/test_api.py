from api.randomm import datasets
from api.client import PaytureClient
from api.errors import errors


class TestExample:

    @staticmethod
    def test_status_code():
        amount = 2000
        month = 10
        year = 22
        orderid = datasets.order_id()
        data = datasets.all_positive(orderid, amount, month, year)
        res = PaytureClient.block(data).status_code

        assert 200 == res

























