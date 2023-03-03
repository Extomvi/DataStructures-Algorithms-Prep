"""
Leetcode Problem 80: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

Using two pointer approach to solve this in place.

Time complexity is O(n)
Space complexity is O(1)
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r+1]:
                r += 1
                count += 1
            slots = min(2, count)
            for i in range(slots):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
