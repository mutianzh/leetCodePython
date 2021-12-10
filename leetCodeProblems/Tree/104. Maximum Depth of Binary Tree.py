"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, curr_depth):
            if not node:
                return

            curr_depth += 1
            if not node.left and not node.right:
                self.max_depth = max(self.max_depth, curr_depth)
            else:
                dfs(node.left, curr_depth)
                dfs(node.right, curr_depth)

            return

        self.max_depth = 1
        curr_depth = 0
        dfs(root, curr_depth)

        return self.max_depth