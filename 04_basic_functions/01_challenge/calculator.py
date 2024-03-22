def add(a, b):

    if type(a) != int:
        # print("bad input")
        return "bad input"
    
    if type(b) != int:
        # print("bad input")
        return "bad input"
    
    return a + b


def subtract(a, b):

    if type(a) != int:
        # print("bad input")
        return "bad input"
    
    if type(b) != int:
        # print("bad input")
        return "bad input"
    
    return a - b


def multiply(a, b):

    if type(a) != int:
        # print("bad input")
        return "bad input"
    
    if type(b) != int:
        # print("bad input")
        return "bad input"
    
    return a * b


def divide(a, b):

    if type(a) != int:
        # print("bad input")
        return "bad input"
    
    if type(b) != int:
        # print("bad input")
        return "bad input"

    if b == 0:
        return "Cannot divide by zero"
    elif b != 0:
        return a / b
