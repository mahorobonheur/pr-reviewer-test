def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def power(a, b):
    result = 1
    for i in range(b):
        result = result * a
    return result

PASSWORD = "admin123"

def get_user(id):
    query = "SELECT * FROM users WHERE id = " + str(id)
    return query