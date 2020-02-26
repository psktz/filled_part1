import datetime


def verifyCreditCardNumber(creditCardNumber):
    # Checks if the parameter is of of type str
    if not isinstance(creditCardNumber, str):
        raise TypeError
    else:
        creditCardNumber.replace(" ", "")
        if not creditCardNumber.isdigit():
            raise ValueError
        # Check if the credit card number has 16 digits
        if len(creditCardNumber) != 16:
            raise ValueError

        # Luhn credit card verification

        # 1. Separate last digit from the string
        lastDigit = int(creditCardNumber[-1])
        firstFifteenDigits = creditCardNumber[:-1]
        # 2. Reverse the remaining string
        firstFifteenDigits = firstFifteenDigits[::-1]

        # 3. Create int list
        firstFifteenDigits = [int(i) for i in firstFifteenDigits]

        # Double all digits at odd indexes
        firstFifteenDigits = [x * 2 if i % 2 else x for i, x in enumerate(firstFifteenDigits, 1)]

        # Subtract 9 from all numbers of 9

        firstFifteenDigits = [x - 9 if x > 9 else x for x in firstFifteenDigits]

        # Sum all numbers
        digitSum = sum(firstFifteenDigits)
        # Check if sum mod 10 equals the previously stored last digit
        if digitSum % 10 != lastDigit:
            raise ValueError
    return True


def verifyCardHolder(cardHolder):
    # Checks if parameter is of type str
    if not isinstance(cardHolder, str):
        raise TypeError


def verifyExpirationDate(expirationDate):
    # Checks if parameter is of type DateTime and that the card is not expired
    if not isinstance(expirationDate, datetime.datetime):
        raise TypeError
    else:
        currentTime = datetime.datetime.now()
        if (expirationDate < currentTime):
            raise ValueError


def verifySecurityCode(securityCode):
    # Checks if the security code has the right type, format and length
    if securityCode == None:
        return None
    elif not isinstance(securityCode, str):
        raise TypeError
    elif not securityCode.isdigit():
        raise ValueError
    elif not len(securityCode) == 3:
        raise ValueError


def verifyAmount(amount):
    # Checks if the amount introduced is of type float and positive
    if not isinstance(amount, float):
        raise TypeError
    if float(amount) <= 0:
        raise ValueError


def SanitizeParameters(data):
    # Sanitization function that returns the required parameters as the desired type
    creditCardNumber = data['CreditCardNumber']
    cardHolder = data['CardHolder']
    expirationDate = datetime.datetime(2000 + int(data['ExpirationDate'][3:5]), int(data['ExpirationDate'][:2]), 1)
    securityCode = data['SecurityCode']
    amount = float(data['Amount'])
    return creditCardNumber, cardHolder, expirationDate, securityCode, amount


def str_converter(o):
    # Functions that allows jsonification of DateTime object
    if isinstance(o, datetime.datetime):
        return o.__str__()
