"""
Maximum subarray
"""
#Using a sliding window to get a O(N) algorithm
def maximum_subarray(nums):
    maxSum = nums[0]
    currentSum = 0

    for n in nums:
        if currentSum < 0: #resetting the value of current sum if the sum is less than 0
            currentSum = 0
        currentSum += n
        maxSum = max(maxSum, currentSum)
    return maxSum


print(maximum_subarray([5,4,-1,7,8]))