"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): return a + b

def subtract(a,b): return a - b

def multiply(a,b): return a * b

def divide(a,b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b/a

def logarithm(a,b):
    assert type(a) == int
    assert type(b) == int
    if AssertionError:
        raise ValueError("Must enter integers")
    return math.log(a, b)

def exponent(a,b): return a**b