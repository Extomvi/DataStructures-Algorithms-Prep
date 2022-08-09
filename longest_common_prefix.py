"""
Longest common prefix in a list
"""
def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]
    strs.sort()
    result = ""
    first = strs[0]
    last = strs[len(strs)-1]
    #print(first, last)
    for i in range(len(first)):
        if first[i] ==  last[i]:
            result = result + first[i]
        else:
            break
    return result

print(longestCommonPrefix(["leetcode", "leets", "leetc", "lettuce"]))