"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by a = 0")

def log(a,b):
    if a <=0 or a ==1:
        raise ValueError("Base must be greater than 0 and not equal to 1")
    if b <= 0:
        raise ValueError("Logarithm undefined for b <= 0")
    return math.log(b,a)

def exp(a,b):

def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

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

def exponent(a,b):

    return a**b