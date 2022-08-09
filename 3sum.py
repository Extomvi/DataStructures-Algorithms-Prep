"""
3 sum of a number
"""
#brute force
def three_sum(nums):
    n = len(nums)
    for i in range(n - 2):
        for j in range(i+1, n - 1):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    return [nums[i], nums[j], nums[k]]
                return -1

#Using 2 pointers
def threeSum(nums):
    if not nums and len(nums) < 3:
        return []
    result = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        twoSum(nums, i, result)
    print(result)
            
def twoSum(nums, i, result):
    left = i + 1
    right = len(nums) - 1
    while left < right:
        total = nums[i] + nums[left] + nums[right]
        if total == 0:
            result.append([nums[i], nums[left], nums[right]])
            left += 1
            right -= 1
            
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif total < 0:
            left += 1
        else:
            right -= 1

print(threeSum([2,3,-1,4,1,-3]))