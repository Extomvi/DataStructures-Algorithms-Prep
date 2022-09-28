"""
The challenge then is to write an algorithm that will read a string of parentheses from left to right and decide whether the symbols are balanced
"""
# Leetcode: https://leetcode.com/problems/valid-parentheses/
from stack import Stack

#For different types of parentheses

def checks(open, close):
    opener = "({["
    closer = ")}]"
    return opener.index(open) == closer.index(close)

def validParentheses(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "({[":
            s.push(symbol)

        else:
            if s.isEmpty():
                return False
            else:
                top = s.pop()
                if not checks(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    
    else:
        return False
    

print(validParentheses('{({([][])}())}'))
print(validParentheses('[{()]'))

#For same type of braces
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