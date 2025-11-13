"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
<<<<<<< HEAD
def square_root(a):
    try:
        result = math.sqrt(a)
        assert a >= 0
    except ValueError:
        print("Variable 'a' must be positive")
    return result

def hypotenuse(a,b):
    math.hypot(a, b)

=======

def add(a,b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by a = 0")

def exp(a,b):
>>>>>>> 08df2cd8c6313ddcdee520bd0a3abb13c4644d9e

def subtract(a,b):
    return a - b

def logarithm(a,b):
    assert type(a) == int
    assert type(b) == int
    if AssertionError:
        raise ValueError("Must enter integers")
    if a <= 0 or a == 1:
        raise ValueError("Variable 'a' can't be negative or equal to 1")
    if b == 0:
        raise ValueError("Variable 'b' can't be equal to 0")
    return math.log(a, b)