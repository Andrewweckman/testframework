class success:
    @staticmethod
    def success(res):
        if 'Success="True"' in res:
            a = 'ok'
            return a
        else:
            a = 'notok'
            return a