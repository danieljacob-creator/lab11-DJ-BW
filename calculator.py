#https://github.com/danieljacob-creator/lab11-DJ-BW
#Partner 1: Daniel Jacobs
#Partner 2: Bryce Williams

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example

def square_root(a):
    if a < 0:
        raise ValueError("Variable 'a' must be positive")
    return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a, b)

def add(a,b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by a = 0")
    return b/a

def exp(a,b):
    return a**b

def subtract(a,b):
    return a - b

def logarithm(a,b):
    if type(a) != int and type(a) != float:
        raise ValueError("Must enter Integers")
    if type(b) != int and type(b) != float:
        raise ValueError("Must enter integers")

    if a <= 0 or a == 1:
        raise ValueError("Variable 'a' can't be negative or equal to 1")
    if b == 0:
        raise ValueError("Variable 'b' can't be equal to 0")
    return math.log(b,a)