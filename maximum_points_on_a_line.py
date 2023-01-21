# Leetcode Problem 149 (Hard): https://leetcode.com/problems/max-points-on-a-line/
"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
"""
from collections import defaultdict
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        numOfPoints = []
        for i in range(len(points)):
            p1 = points[i]
            # hashmap to keep track of the available slopes and the number of points that fall in that slope category
            count = defaultdict(int)
            for j in range(i+1, len(points)):
                p2 = points[j]
                # when the points on the X axis are the same, then we set the slope to be infinity because we can't divide the y axis component by 0
                if p2[0] == p1[0]:
                    slope = float("inf")
                else:
                    # calculating the slope using the formular y2-y1 / x2-x1 
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                # set the slope count in the hashmap and increment it by 1 once we get the point with the same slope
                count[slope] += 1
                numOfPoints.append(count[slope]+1)
        return max(numOfPoints) if len(numOfPoints) != 0 else 1