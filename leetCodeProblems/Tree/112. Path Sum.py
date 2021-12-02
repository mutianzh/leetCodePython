"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def has_sum(node, path_sum, targetSum):
            if not node.left and not node.right:
                return path_sum + node.val == targetSum

            if node.left and has_sum(node.left, path_sum + node.val, targetSum):
                return True

            if node.right and has_sum(node.right, path_sum + node.val, targetSum):
                return True

            return False

        return has_sum(root, 0, targetSum)