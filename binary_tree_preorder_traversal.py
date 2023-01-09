"""
Leetcode Problem 144: https://leetcode.com/problems/binary-tree-preorder-traversal/description/

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example:
Input: root = [1,null,2,3]
Output: [1,2,3]
"""
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive solution
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        self.bfs(root, stack)
        return stack
    def bfs(self, node, stack):
        if not node:
            return None
        stack.append(node.val)
        if node.left:
            self.bfs(node.left, stack)
        if node.right:
            self.bfs(node.right, stack)

# iterative
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        stack = [root]
        output = []
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return output