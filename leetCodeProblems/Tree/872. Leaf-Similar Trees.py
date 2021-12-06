"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
Example 1:

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:

Input: root1 = [1], root2 = [1]
Output: true
Example 3:

Input: root1 = [1], root2 = [2]
Output: false
Example 4:

Input: root1 = [1,2], root2 = [2,2]
Output: true
Example 5:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(node, leaf_list):
            if not node:
                return

            if not node.left and not node.right:
                leaf_list.append(node.val)
                return

            dfs(node.left, leaf_list)
            dfs(node.right, leaf_list)

            return

        if not root1 or not root2:
            return False

        leaf_1 = []
        leaf_2 = []

        dfs(root1, leaf_1)
        dfs(root2, leaf_2)

        if len(leaf_1) == len(leaf_2):
            for i in range(len(leaf_1)):
                if leaf_1[i] != leaf_2[i]:
                    return False

            return True


        else:
            return False