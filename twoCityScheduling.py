"""
Two City Scheduling -> (https://leetcode.com/problems/two-city-scheduling/)

A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

 

Example 1:

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
"""
# Time complexity is O(nlogN) | Space complexity is O(logn)
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # we need to sort the costs list in ascending order by the difference between the aCosti and bCosti
        # the sorting will enable us have the smallest on the index 0 and largest on index 1
        # after sorting the lists should be even
        
        """
        costs = [[10,20],[30,200],[400,50],[30,20]]
        
        costs => [[-1700], [-10], [10], [350]] => [[30,200], [10,20], [30,20], [400,50]]
        
        -> aCost0 + bCost2 = 30+20 = 50
        -> aCost1 + bCost3 = 10+50 = 60
        -> minimumCost = 50+60 = 110
        """
        costs.sort(key=lambda X: X[0] - X[1])
        n = len(costs) // 2
        minimumCost = 0
        
        for i in range(n):
            aCost = costs[i][0]
            bCost = costs[i+n][1]
            minimumCost += aCost + bCost
        return minimumCost