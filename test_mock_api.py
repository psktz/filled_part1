from payment import Payment
from helper_functions import SanitizeParameters

data = {'CreditCardNumber': '4556737586899855',
        'CardHolder': 'Andrei Puscuta',
        'ExpirationDate': "08/22",
        'SecurityCode': '333',
        'Amount': 25.53}

creditCardNumber, cardHolder, expirationDate, securityCode, amount = SanitizeParameters(data)


def test_CorrectGatewayIsUsedForLessThan20GBP(mocker):
    amount = 19.5
    payment = Payment(creditCardNumber, cardHolder, expirationDate, securityCode, amount)
    mocked_func = mocker.patch('cheapPaymentGateway.CheapPaymentGateway.processPayment')
    payment.process()
    mocked_func.assert_called()


def test_CorrectGatewayIsUsedFor21_500GBP(mocker):
    amount = 21.3
    payment = Payment(creditCardNumber, cardHolder, expirationDate, securityCode, amount)
    mocked_func = mocker.patch('expensivePaymentGateway.ExpensivePaymentGateway.processPayment')
    payment.process()
    mocked_func.assert_called()


def test_CorrectGatewayIsUsedForOver500GBP(mocker):
    amount = 521.25
    payment = Payment(creditCardNumber, cardHolder, expirationDate, securityCode, amount)
    mocked_func = mocker.patch('premiumPaymentGateway.PremiumPaymentGateway.processPayment')
    payment.process()
    mocked_func.assert_called()


def test_ExpensivePaymentGatewayRetriesOnCheapOne(mocker):
    amount = 25.23
    payment = Payment(creditCardNumber, cardHolder, expirationDate, securityCode, amount)
    mocked_func = mocker.patch('expensivePaymentGateway.ExpensivePaymentGateway.processPayment')
    mocked_func2 = mocker.patch('cheapPaymentGateway.CheapPaymentGateway.processPayment')
    payment.process()
    mocked_func.assert_called()
    mocked_func2.assert_called()


def test_PremiumPaymentGatewayRetriesThreeTimes(mocker):
    amount = 521.25
    payment = Payment(creditCardNumber, cardHolder, expirationDate, securityCode, amount)
    mocked_func = mocker.patch('premiumPaymentGateway.PremiumPaymentGateway.processPayment')
    payment.process()
    assert len(mocked_func.call_args_list) == 4
