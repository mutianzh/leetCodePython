"""
199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:
Input: root = []
Output: []
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
#         # solution 1: two queues
#         if not root:
#             return []
#         next_queue = collections.deque([root,])
#         right_side = []
#         while next_queue:
#             curr = next_queue
#             next_queue = collections.deque()
#             while curr:
#                 # went through each node in current level from left right
#                 # record all children from left to right of next level
#                 node = curr.popleft()
#                 if node.left:
#                     next_queue.append(node.left)
#                 if node.right:
#                     next_queue.append(node.right)

#             # when while breaks, node is storing the right most child of this level
#             right_side.append(node.val)


#         return right_side


#         # solution 2: maintain length of a level
#         if not root:
#             return []

#         right_side = []
#         queue = collections.deque([root,])

#         while queue:
#             for i in range(len(queue)):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)

#             right_side.append(node.val)

#         return right_side

# solution 3: recursive dfs