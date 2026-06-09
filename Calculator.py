def add(a, b, c):
    return a + b + c

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def power(a, b):
    result = 1
    for i in range(b):
        result = result * a
    return result



def get_user(id):
    query = "SELECT * FROM users WHERE id = ?"
    return query

def modulus(a, b):
    return a % b

def multiply(a, b, c):
    return a * b

def ask_question(a):
    b = "How are you " + a
    return b + 1