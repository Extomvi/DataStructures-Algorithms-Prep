"""
Top K
"""
# (nlogn)  time complexity solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        valMap = {}
        for n in nums:
            if n not in valMap:
                valMap[n] = 0
            valMap[n] += 1
        print(valMap)
        values = [ key for key,value in sorted(valMap.items(), key=lambda X: X[1], reverse = True)]
        # print(values)
        return values[:k]

