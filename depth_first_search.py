"""
Implementing Depth First Search
"""

# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Using a stack (LIFO) approach.
        stack = [self]
        while stack:
            node = stack.pop()
            array.append(node.name)
            stack.extend(reversed(node.children))
        return array

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Time complexity is O(v + e) | Space complexity is O(v)
    def depthFirstSearch(self, array):
        # Using recursion.
        node = self.name
        array.append(node)
        for child in self.children:
            child.depthFirstSearch(array)
        return array