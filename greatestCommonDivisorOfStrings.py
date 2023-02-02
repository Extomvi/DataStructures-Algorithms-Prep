# Greatest Common Divisor of Strings
"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        lenStr1, lenStr2 = len(str1), len(str2)
        
        def canBeDivided(index):
            if lenStr1 % index or lenStr2 % index:
                return False
            div1, div2 = lenStr1//index, lenStr2//index
            return str1[:index] * div1 == str1 and str1[:index] * div2 == str2

        for i in range(min(lenStr1, lenStr2), 0, -1):
            if canBeDivided(i):
                return str1[:i]
        return ""
