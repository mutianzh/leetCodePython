"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
Example 1:
Input: n = 3
Output: 5
Example 2:
Input: n = 1
Output: 1
"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        G = [0] * (n + 1)
        G[0] = 1  # if root is None, only one unique tree
        G[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]

        return G[n]
