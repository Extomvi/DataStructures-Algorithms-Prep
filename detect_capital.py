"""
Detect capital letter
Case A -> All caps("USA")
Case B -> all not caps("leetcode")
Case C -> Only first letter of word in caps("Google")
"""

def detectCapital(word):
    n = len(word)
        
    #edge case
    if n == 1:
        return True
    
    #case A -> All caps
    if word[0].isupper() and word[1].isupper():
        for i in range(2, n):
            if word[i] is not word[i].isupper():
                return False

    
    #case C -> Only first letter in word is in caps
    else:
        for i in range(1, n):
            if word[i].isupper():
                return False

    #case B -> All not caps
    return True

print(detectCapital("tomiwa"))