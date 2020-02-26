from flask import Flask, request
from payment import Payment
from helper_functions import SanitizeParameters

app = Flask(__name__)


@app.route('/', methods=['POST'])
def ProcessPayment():
    data = request.form
    creditCardNumber, cardHolder, expirationDate, securityCode, amount = SanitizeParameters(data)
    try:
        payment = Payment(creditCardNumber, cardHolder, expirationDate, securityCode, amount)
        print("uptest")
        result = payment.process()
        print("test")
        if result.status_code == 200:
            return "Payment is processed : 200 OK", 200
    except (TypeError, ValueError) as e:
        return "The request is invalid: 400 bad request", 400
    except:
        return "500 internal server error", 500
    return "500 internal server error", 500


if __name__ == '__main__':
    app.run()
