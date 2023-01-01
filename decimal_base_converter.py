"""
Decimal to base converter
"""
from stack import Stack

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"
    stack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        stack.push(rem)
        decNumber = decNumber//base

    baseValue = ""
    while not stack.isEmpty():
        baseValue = baseValue + digits[stack.pop()]
    return baseValue


print(baseConverter(73,2))