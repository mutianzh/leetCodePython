"""
314. Binary Tree Vertical Order Traversal
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:
Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
Example 4:
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
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        min_column, max_column = 0, 0

        # Each element in queue stores (node, column)
        queue = collections.deque([(root, 0)])
        column_table = collections.defaultdict(list)

        while queue:
            node, column = queue.popleft()

            if node is not None:
                min_column = min(min_column, column)
                max_column = max(max_column, column)
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
                column_table[column].append(node.val)

        return [column_table[i] for i in range(min_column, max_column + 1)]