"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:
Input: root = []
Output: true
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return 0, True

            left_depth, left_balance = helper(node.left)
            right_depth, right_balance = helper(node.right)

            diff = abs(left_depth - right_depth)

            is_balance = diff <= 1 and left_balance and right_balance
            depth = max(left_depth, right_depth) + 1

            return depth, is_balance

        d, is_balance = helper(root)

        return is_balance