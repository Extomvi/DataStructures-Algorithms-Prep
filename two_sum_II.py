"""
Two Sum II (sorted array)
"""

def two_sum(numbers, target):
    #using left and right pointers to get a linear algorithm O(N)
    l = 0
    r = len(numbers) - 1

    while l < r:
        currSum = numbers[l] + numbers[r]

        if currSum == target:
            return [l+1, r+1] #because the indexes are starting from 1 and not 0

        elif currSum > target:
            r -= 1

        else:
            l += 1
    return []

print(two_sum([1,3,4,5,7,10,11],9))