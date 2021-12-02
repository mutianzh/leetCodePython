"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
"""

import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def preorder(node, cur_sum, targetSum, h):

            if not node:
                return

            # situation 1
            cur_sum += node.val
            if cur_sum == targetSum:
                self.count += 1

            # situation 2
            self.count += h[cur_sum - targetSum]

            # update prefix
            h[cur_sum] += 1

            # check left and right
            preorder(node.left, cur_sum, targetSum, h)
            preorder(node.right, cur_sum, targetSum, h)

            h[cur_sum] -= 1

        self.count = 0
        h = collections.defaultdict(int)
        preorder(root, 0, targetSum, h)

        return self.count