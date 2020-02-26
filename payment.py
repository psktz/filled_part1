from cheapPaymentGateway import CheapPaymentGateway
from expensivePaymentGateway import ExpensivePaymentGateway
from premiumPaymentGateway import PremiumPaymentGateway
import helper_functions as fct


class Payment:
    """
    Class used to conceptualize a payment

    Attributes:
        - CreditCardNumber : str
            the 16 digit number present on the front of a debit/credit card
        - CardHolder : str
            the name of the owner of the card making the payment
        - ExpirationDate : DateTime
            the date at which the card must be renewed
        - SecurityCode : str
            3 digit code found on the back of the debit/credit card
        - Amount :
            the sum of money that is used for the payment
    Methods:
        - Process : boolean
            function that redirects the payment details to the appropriate payment gateway
    """
    creditCardNumber = ""
    cardHolder = ""
    expirationDate = None
    securityCode = ""
    amount = 0
    paymentGateway = None

    def __init__(self, creditCardNumber, cardHolder, expirationDate, securityCode, amount):
        fct.verifyCreditCardNumber(creditCardNumber)
        fct.verifyCardHolder(cardHolder)
        fct.verifyExpirationDate(expirationDate)
        fct.verifySecurityCode(securityCode)
        fct.verifyAmount(amount)

        self.creditCardNumber = creditCardNumber
        self.cardHolder = cardHolder
        self.expirationDate = expirationDate
        self.securityCode = securityCode
        self.amount = amount

    def process(self):
        if self.amount <= 20:
            gateway = CheapPaymentGateway()
            r = gateway.processPayment(self)
        elif 20 < self.amount < 500:
            gateway = ExpensivePaymentGateway()
            r = gateway.processPayment(self)
            if r.status_code != 200:
                gateway = CheapPaymentGateway()
                r = gateway.processPayment(self)
        else:
            gateway = PremiumPaymentGateway()
            r = gateway.processPayment(self)
            if r.status_code != 200:
                counter = 0
                while counter < 3 and r.status_code != 200:
                    r = gateway.processPayment(self)
                    print(counter)
                    counter += 1
        return r
