"""
Two sum
"""
# Leetcode: https://leetcode.com/problems/two-sum/

#Brute force O(N^2)
def twoSum(nums, target):
    #bruteforce solution
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            val = target - nums[i]
            if nums[j] == val:
                return [i,j]

# Optimized code O(N)
def twoSum(nums, target):
    #Using a dictionary O(N)
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        seen[nums[i]] = i

# Using HashMap O(N)
def two_sum(nums, target):
    prevMap = {} #key:valye pair
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return []
    

print(two_sum([2,7,11,15],9))