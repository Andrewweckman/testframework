from faker import Faker
import strgen



faker = Faker()


class datasets:

        @staticmethod
        def all_positive(orderid, amount, month, year):

            Key = "Merchant"
            OrderId = orderid
            Amount  = amount
            PAN = 4111111111111112
            EMonth = month
            EYear = year

            return {'Key': Key,
                    'Amount': Amount,
                    'OrderId': OrderId,
                    'PayInfo': 'PAN=' + str(PAN) + ';' + 'EMonth=' + str(EMonth) + ';' + 'EYear=' + str(EYear)+';'+'OrderId='+ OrderId +';' + 'Amount=' + str(Amount)
                    }

        @staticmethod
        def order_id():
            return strgen.StringGenerator("[\-\w]{30}").render()








