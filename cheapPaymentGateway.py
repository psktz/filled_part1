import json
import requests
from helper_functions import str_converter


class CheapPaymentGateway():
    """
    The class that represents the gateway used to process a payment below 20 GBP
    """
    def processPayment(self, paymentDetails):
        json_format =  json.dumps(paymentDetails, default= str_converter)
        r = requests.post("http://www.google.com", json = json_format)
        print("Cheap gateway was used")
        return r
