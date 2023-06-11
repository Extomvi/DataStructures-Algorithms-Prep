"""
Palindrome checker for strings
"""
# Time complexity is O(n)
# Space complexity is O(n)
from collections import deque
def palchecker(aString):
    q = deque()

    for c in aString:
        q.appendleft(c)

    balanced = True
    while len(q) > 1 and balanced:
        first = q.pop()
        last = q.popleft()
        if first != last:
            balanced = False

    return balanced
    # l, r = 0, len(q) - 1
    # for i in range(len(q)):
    #     if q[l] == q[r]:
    #         l+= 1
    #         r-= 1
    #     else:
    #         return False
    # return True

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))