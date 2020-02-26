import requests
import datetime

dictToSend = {'name': 'Andrei'}
odata = datetime.datetime(2021, 1, 1)
res = requests.post('http://localhost:5000/', data={'CreditCardNumber': '4556737586899855',
                                                    'CardHolder': 'Andrei Puscuta',
                                                    'ExpirationDate': "08/22",
                                                    'SecurityCode': '333',
                                                    'Amount': 555.53})
print(res)
