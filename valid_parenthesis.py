"""
The challenge then is to write an algorithm that will read a string of parentheses from left to right and decide whether the symbols are balanced
"""
from stack import Stack
def valid_parenthesis(symbolString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(valid_parenthesis('((()))'))