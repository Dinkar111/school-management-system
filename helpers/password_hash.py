import hashlib


def make_pw_hash(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_pw_hash(password, hashed):
    if make_pw_hash(password) == hashed:
        return True
    return False
