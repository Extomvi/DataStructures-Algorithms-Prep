"""
Two sum
"""
#Brute force O(n2)
def twoSum(nums, target):
    #bruteforce solution
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            val = target - nums[i]
            if nums[j] == val:
                return [i,j]

#Optimized code
def twoSum(nums, target):
    #Using a dictionary O(N)
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        seen[nums[i]] = i

print(twoSum([2,7,11,15],9))