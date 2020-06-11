from api.randomm import datasets
from api.client import PaytureClient
from api.errors import errors
from api.success import success


class TestExample:

    @staticmethod
    def test_status_code1():
        amount = 2000
        month = 10
        year = 22
        orderid = datasets.order_id()
        data = datasets.all_positive(orderid, amount, month, year)
        res = PaytureClient.block(data).status_code

        assert 200 == res

    @staticmethod
    def test_success_amount():
        amount = 123456789
        month = 10
        year = 22
        orderid = datasets.order_id()
        data = datasets.all_positive(orderid, amount, month, year)
        res = PaytureClient.block(data).text

        success.success(res)

        assert 'ok' == success.success(res)

    @staticmethod
    def test_success_amount_1():
        amount = 1
        month = 10
        year = 22
        orderid = datasets.order_id()
        data = datasets.all_positive(orderid, amount, month, year)
        res = PaytureClient.block(data).text

        success.success(res)

        assert 'ok' == success.success(res)

    @staticmethod
    def test_success_amount_2():
        amount = 11
        month = 10
        year = 22
        orderid = datasets.order_id()
        data = datasets.all_positive(orderid, amount, month, year)
        res = PaytureClient.block(data).text

        success.success(res)

        assert 'ok' == success.success(res)

    @staticmethod
    def test_success_amount_3():
        amount = 111
        month = 10
        year = 22
        orderid = datasets.order_id()
        data = datasets.all_positive(orderid, amount, month, year)
        res = PaytureClient.block(data).text

        success.success(res)

        assert 'ok' == success.success(res)

    @staticmethod
    def test_success_amount_7():
        amount = 1234567
        month = 10
        year = 22
        orderid = datasets.order_id()
        data = datasets.all_positive(orderid, amount, month, year)
        res = PaytureClient.block(data).text

        success.success(res)

        assert 'ok' == success.success(res)

    @staticmethod
    def test_success_amount_abc():
        amount = 'abc'
        month = 10
        year = 22
        orderid = datasets.order_id()
        data = datasets.all_positive(orderid, amount, month, year)
        res = PaytureClient.block(data).text

        errors.error_amount(res)

        assert 'ok' == errors.error_amount(res)