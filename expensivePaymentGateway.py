import json
import requests
from helper_functions import str_converter


class ExpensivePaymentGateway():
    """
       The class that represents the gateway used to process a payment over 20 GBP but under 500 GBP
    """

    def processPayment(self, paymentDetails):
        json_format = json.dumps(paymentDetails, default=str_converter)
        r = requests.post("http://www.google.com", json=json_format)
        return r
