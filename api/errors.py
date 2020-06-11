class errors:

    @staticmethod
    def error_dulicate_id(res):
        if 'ErrCode="DUPLICATE_ORDER_ID"' in res:
            a = 'ok'
            return a
        else:
            a = 'notok'
            return a

    @staticmethod
    def error_access_denied(res):
        if 'ErrCode="ACCESS_DENIED"' in res:
            a = 'ok'
            return a
        else:
            a = 'notok'
            return a

    @staticmethod
    def error_access_denied(res):
        if 'ErrCode="ACCESS_DENIED"' in res:
            a = 'ok'
            return a
        else:
            a = 'notok'
            return a

    @staticmethod
    def error_amount(res):
        if 'ErrCode="AMOUNT_ERROR"' in res:
            a = 'ok'
            return a
        else:
            a = 'notok'
            return a

