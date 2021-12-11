"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""

import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        #         # dfs approach
        #         self.min = float('inf')
        #         def dfs(node, depth):
        #             if not node:
        #                 self.min = min(self.min, depth)
        #                 return

        #             depth += 1
        #             if not node.left and not node.right:
        #                 # this is the leaf
        #                 self.min = min(depth, self.min)
        #                 return

        #             if node.left:
        #                 dfs(node.left, depth)

        #             if node.right:
        #                 dfs(node.right, depth)

        #             return

        #         dfs(root, 0)

        #         return self.min

        # bfs approach
        if not root:
            return 0

        queue = collections.deque()
        queue.append(root)
        next_queue = collections.deque()
        min_depth = 0
        while queue:
            min_depth += 1
            while queue:
                cur_node = queue.popleft()
                if not cur_node.left and not cur_node.right:
                    return min_depth

                if cur_node.left:
                    next_queue.append(cur_node.left)
                if cur_node.right:
                    next_queue.append(cur_node.right)

            queue = next_queue
            next_queue = collections.deque()

        return min_depth