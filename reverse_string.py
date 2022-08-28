"""
Reverse string in constant space and in constant time
"""

#Leetcode: https://leetcode.com/problems/reverse-string/

def reverseString(s):
    #using a recursive function 
    # time is O(N), space is O(N)
    def helper(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
            helper(left, right)

    helper(0, len(s) - 1)
    return s

def reverse_string(s):
    #using 2 pointer approach to slide through
    #time is O(N), space is O(1)
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1

    return s


print("Using recursive approach gives: ", reverseString(['h','e','l','l','o']))
print("Using 2 pointer approach to slide across gives: ", reverse_string(['h','e','l','l','o']))