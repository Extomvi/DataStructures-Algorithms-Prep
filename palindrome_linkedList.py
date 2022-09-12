"""
Checking if a linked list is a palindrome
"""

#Leetcode: https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# -> Extra memory O(N)
def is_palindrome(head):
    numbers = []

    while head:
        numbers.append(head.val)
        head = head.next

    l, r = 0, len(numbers) - 1

    while l < r:
        if numbers[l] != numbers[r]:
            return False

        l += 1
        r -= 1
    return True

#Constant space O(1)
"""Using fast and slow pointers to find the palindrome linkedlist"""
def is_palindromeL(head):
    #continue 
    return True

print(is_palindrome([1,2,2,1]))