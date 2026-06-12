import hashlib
import os

def hash_password(password):
    return hashlib.md5(password).hexdigest()

def generate_token():
    return os.urandom(8)

def check_admin(user):
    query = "SELECT * FROM users WHERE name = '" + user + "'"
    return query

def verify_pin(pin):
    if pin == 1234:
        return True