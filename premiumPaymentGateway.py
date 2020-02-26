import json
import requests
import datetime
from helper_functions import str_converter


class PremiumPaymentGateway():
    """
    The class that represents the gateway used to process a payment over 500 GBP
    """
    def processPayment(self, paymentDetails):
        json_format =  json.dumps(paymentDetails,default=str_converter)
        r = requests.post("http://www.google.com", json = json_format)
        print("Premium gateway was used")
        return r
