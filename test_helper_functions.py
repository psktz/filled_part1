import pytest
import helper_functions as h
import datetime


def test_CardNumberInputIsString():
    with pytest.raises(TypeError):
        h.verifyCreditCardNumber(1234567812345670)


def test_CardNumberContainsOnlyDigits():
    with pytest.raises(ValueError):
        h.verifyCreditCardNumber("12345678123456h7")


def test_CardNumberLengthIsEqualTo16():
    with pytest.raises(ValueError):
        h.verifyCreditCardNumber("123456781234567")


def test_ShouldFailLuhnAlgortihm():
    with pytest.raises(ValueError):
        assert h.verifyCreditCardNumber("1234567812345678") == False


def test_ShouldPassLuhnAlgorithm():
    assert h.verifyCreditCardNumber("1234567812345670") == True


def test_CardHolderInputIsString():
    with pytest.raises(TypeError):
        h.verifyCardHolder(24)


def test_ExpirationDateIsOfTypeDateTime():
    with pytest.raises(TypeError):
        h.verifyExpirationDate("22/02/2022")


def test_CheckCardIsNotExpired():
    with pytest.raises(ValueError):
        h.verifyExpirationDate(datetime.datetime(2019, 1, 1))


def test_CheckGoodCreditCardIsNotExpired():
    h.verifyExpirationDate(datetime.datetime(9999, 1, 1))


def test_CheckIfSecurityCodeIsString():
    with pytest.raises(TypeError):
        h.verifySecurityCode(999)


def test_CheckIfSecurityCodeContainsOnlyDigits():
    with pytest.raises(ValueError):
        h.verifySecurityCode("2a3")


def test_CheckIfSecurityCodeLenthIsEqualToThree():
    with pytest.raises(ValueError):
        h.verifySecurityCode("1234")


def test_CheckIfAmountIsOfTypeFloat():
    with pytest.raises(TypeError):
        h.verifyAmount("23")
        h.verifyAmount(25)
