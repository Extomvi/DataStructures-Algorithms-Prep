"""
Implementing the Breadth First Search Algorithm
"""
# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Time complexity is O(v + e) | Space complexity is O(v)
    def breadthFirstSearch(self, array):
        # Using list to represent my queue (FIFO).
        queue = [self]
        while queue:
            currentNode = queue.pop(0)
            array.append(currentNode.name)
            for child in currentNode.children:
                queue.append(child)
        return array

    
from collections import deque
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Using deque to represent my queue.
        queue = deque([self])
        while queue:
            currentNode = queue.popleft()
            array.append(currentNode.name)
            for child in currentNode.children:
                queue.append(child)
        return array