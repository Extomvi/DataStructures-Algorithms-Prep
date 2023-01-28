# Leetcode Problem 352: https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
"""
Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:

SummaryRanges() Initializes the object with an empty stream.
void addNum(int value) Adds the integer value to the stream.
int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
 
"""
from sortedcontainers import SortedDict
class SummaryRanges:

    def __init__(self):
        self.items = SortedDict()
        

    def addNum(self, value: int) -> None:
        self.items[value] = True

    def getIntervals(self) -> List[List[int]]:
        result = []
        for n in self.items:
            if result and result[-1][1] + 1 == n:
                result[-1][1] = n
            else:
                result.append([n, n])

        return result
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
