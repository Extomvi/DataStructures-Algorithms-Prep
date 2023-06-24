"""
Reversing a word in a string
"""
# Time complexoty is O(n) | Space complexity is O(n)

from stack import Stack

def revstring(mystr):
    myStack = Stack()
    revString = ''
    for char in mystr:
        myStack.push(char)
    while not myStack.isEmpty():
        revString = revString + myStack.pop()
    return revString
        

print(revstring('apple'),'elppa')
print(revstring('x'),'x')
print(revstring('1234567890'),'0987654321')
