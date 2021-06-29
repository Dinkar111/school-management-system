from helpers.validations import email_validation, password_validation, phone_validation


def test_validate_wrong_email():
    email = "drasgmac.om"
    check = email_validation(email)
    assert not check


def test_validate_right_email():
    email = "dinkar@gmail.com"
    check = email_validation(email)
    assert check


def test_validate_wrong_phone():
    phone = "989892311111"
    check = phone_validation(phone)
    assert not check


def test_validate_right_phone():
    phone = "9877665511"
    check = phone_validation(phone)
    assert check


def test_validate_wrong_password():
    password = "dinkar"
    check = password_validation(password)
    assert not check


def test_validate_right_password():
    password = "Dinkar@123"
    check = password_validation(password)
    assert check


