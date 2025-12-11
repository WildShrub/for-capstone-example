import MATH

def add (a,b):
    return a+b

def subtract (a,b):
    return a-b

def multiply (a,b): 
    return a*b

def divide (a,b):
    if b == 0:
        return "Error: Division by zero"
    return a/b

def log (a,b):
    if a <= 0 or b <= 0 or b == 1:
        return "Error: Invalid input for logarithm"
    return MATH.log(a,b)

def square (a):
    return a^2

def sin (a):
    return MATH.sin(a)

def cos (a):
    return MATH.cos(a)

def square_root (a):
    if a < 0:
        return "Error: Negative input for square root"
    return MATH.square_root(a)

def percentage (a,b):
    if b == 0:
        return "Error: Division by zero"
    if a < 0 or b < 0:
        return "Error: Negative input for percentage"
    return (a / b) * 100
    