"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursion:
        def helper(node, ans):
            if not node:
                return

            helper(node.left, ans)
            helper(node.right, ans)
            ans.append(node.val)

            return

        ans = []
        helper(root, ans)

        return ans

