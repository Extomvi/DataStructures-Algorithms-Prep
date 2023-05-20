"""Reverse word in a string III"""

# Leetcode: https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Time Complexity is O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        rev_string = (
             s[::-1]               # Character reverse
             .split(' ')[::-1]     # Array reverse
        )
        return " ".join(rev_string)
        
def reverseWords(s):
    rev_string = s[::-1]
    revString = rev_string.split(" ")
    revString = revString[::-1]

    return " ".join(revString)
 
print(reverseWords("running around"))
