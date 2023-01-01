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

# O(N) solution using another dictionary and putting the frequency as key in the dictionary mapping
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        dict2 = {}
        output = []
        for n in nums:
            if n not in numMap:
                numMap[n] = 0
            numMap[n] += 1
        

        for key, values in numMap.items():
            if values in dict2:
                dict2[values].append(key)
            else:
                dict2[values] = [key]
       
        maxVal = max(dict2.keys())
        for i in range(maxVal, -1, -1):
            if i in dict2:
                output += dict2[i]
            if len(output) == k:
                return output

