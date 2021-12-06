"""
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.

Example 1:
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, leaf_dict):
            if not node:
                return -1

            left = dfs(node.left, leaf_dict)
            right = dfs(node.right, leaf_dict)
            level = max(left, right) + 1
            leaf_dict[level].append(node.val)
            return level

        leaf_dict = collections.defaultdict(list)
        dfs(root, leaf_dict)
        ans = []
        for key in leaf_dict.keys():
            ans.append(leaf_dict[key])

        return ans