"""Reverse word in a string III"""
class Solution:
    def reverseWords(self, s: str) -> str:
        rev_string = s[::-1]
        revString = rev_string.split(" ")
        revString = revString[::-1]
        
        return " ".join(revString)
 
        