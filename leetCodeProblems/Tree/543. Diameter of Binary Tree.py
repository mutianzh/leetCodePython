"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def longest_path_to_leaf(node):
            if not node:
                return 0

            path_to_left = longest_path_to_leaf(node.left)
            path_to_right = longest_path_to_leaf(node.right)

            longest_path = max(path_to_left, path_to_right) + 1
            cur_diameter = path_to_left + path_to_right
            self.diameter = max(self.diameter, cur_diameter)

            return longest_path

        longest_path_to_leaf(root)

        return self.diameter

