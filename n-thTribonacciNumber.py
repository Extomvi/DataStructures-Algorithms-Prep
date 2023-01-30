"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        # creating an initial sequence
        sequence = [0,1,1]
        if n < 3:
            return sequence[n]
        for i in range(3, n+1):
            sequence[0], sequence[1], sequence[2] = sequence[1], sequence[2], sum(sequence)
        return sequence[-1]
