"""
Decimal to binary converter using stack
"""
from stack import Stack
def decConverter(number):
    # s = Stack()

    # while number > 0:
    #     rem = number % 2
    #     s.push(rem)
    #     number = number // 2

    # binaryV = ""
    # while not s.isEmpty():
    #     binaryV = binaryV + str(s.pop())
    # return binaryV
    stack = []
    while number > 0:
        rem = number % 2
        stack.append(rem)
        number = number // 2

    binaryV = ""
    while stack:
        binaryV = binaryV + str(stack.pop())
    return binaryV

    
print(decConverter(42))