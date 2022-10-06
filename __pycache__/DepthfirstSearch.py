# The DFS is a recursive algoruth that uses the idea of backtracking.
# It involves exhaustive searches of all the nodes by going ahead, if possible, else by backtracking.
# Backtrack means moving forward and there's no more node along the current path,
# You move backwards on the smae path to find nodes to traverse.

def dfs (graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for i in graph[start]:
        if i not in visited:
            dfs(graph, i, visited)
        return visited

graph = {0: [2], 1: [0,2], 2: [3], 3: [1,2]}
dfs(graph, 2) # 1 0 2 3