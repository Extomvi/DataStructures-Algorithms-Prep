"""
Reversing a word in a string
"""

# from test import testEqual
# from pythonds.basic import Stack
import stack

def revstring(mystr):
    myStack = Stack()
    revString = ''
    for char in mystr:
        myStack.push(char)
    while not myStack.isEmpty():
        revString = revString + myStack.pop()
    return revString
        

testEqual(revstring('apple'),'elppa')
testEqual(revstring('x'),'x')
testEqual(revstring('1234567890'),'0987654321')
