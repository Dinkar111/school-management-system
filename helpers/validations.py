import re


# Validate email : example: example@example.com
def email_validation(email):
    pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.[a-z]"
    if re.search(pattern, email):
        return True
    else:
        print("\n   Invalid Email")


# Validate phone : must be 10 digits and integer
def phone_validation(phone):
    if not re.search("[0-9]", phone):
        print("\n   Phone number must be number")
    elif len(phone) != 10:
        print("\n   Phone number must be 10 digits")
    else:
        return True


# Validate password : password must be greater than 8, capitalized, must have digits
def password_validation(password):
    if not len(password) > 8 and not len(password) < 20:
        print("\n   Password must be greater than 8 digits and less than 20")
    elif not any(character.islower() for character in password):
        print("\n   Password should have at least one character lower case")
    elif not any(character.isupper() for character in password):
        print("\n   Password should have at least one character upper case")
    elif not any(character.isdigit() for character in password):
        print("\n   Password should have at least one number")
    elif not any(character in ['@', '$', '#'] for character in password):
        print("\n   Password should have at least one special character [@, $, #]")
    else:
        return True
