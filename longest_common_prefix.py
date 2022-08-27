"""
Longest common prefix in a list
"""
# Leetcode: https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]
    strs.sort()
    result = ""
    first = strs[0]
    last = strs[len(strs)-1]
    for i in range(len(first)):
        if first[i] !=  last[i]:
            break
        result = result + first[i]
    return result

print(longestCommonPrefix(["leetcode", "leets", "leetc", "lettuce"]))