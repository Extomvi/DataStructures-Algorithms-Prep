"""Reverse word in a string III"""
def reverseWords(s):
    rev_string = s[::-1]
    revString = rev_string.split(" ")
    revString = revString[::-1]

    return " ".join(revString)
 
print(reverseWords("running around"))