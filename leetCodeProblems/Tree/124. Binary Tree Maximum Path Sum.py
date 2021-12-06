"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.
Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = -float('inf')

        def max_path(node):

            if not node:
                return 0

            path_left = max_path(node.left)
            path_right = max_path(node.right)

            max_sum = max(path_left, path_right)
            if max_sum <= 0:
                max_sum = node.val

            else:
                max_sum += node.val

            cur_max_sum = node.val + max(0, path_left) + max(0, path_right)

            self.max_path_sum = max(self.max_path_sum, cur_max_sum)
            return max_sum

        max_path(root)

        return self.max_path_sum