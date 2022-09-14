"""
Climbing stairs problem
"""

# Leetcode: https://leetcode.com/problems/climbing-stairs/

def climbingStairs(n):
    """
                n
                /\
               1  2
              /\  /\
             1  2 1 2
    """
    one, two = 1, 1

    for i in range(n - 1):
        temporary = one
        one = one + two
        two = temporary

    return one

print(climbingStairs(2))