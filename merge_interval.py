"""
Merge interval (https://leetcode.com/problems/merge-intervals/)
"""

# Using the sorting method and comparing values
# Time complexity is O(nlogn) -> because of the sorting operation
# Space complexity is O(n)

def merge_sort(intervals):
    #sorting the intervals which is log n
    intervals.sort(key=lambda x: x[0])
    merge = []
    for interval in intervals:
        if not merge or merge[-1][1] < interval[0]:
            merge.append(interval)
        else:
            merge[-1][1] = max(merge[-1][1], interval[1])
    return merge

print(merge_sort([[1,3],[2,6],[8,10],[15,18]]))
