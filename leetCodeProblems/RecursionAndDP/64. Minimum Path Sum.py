"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid:
            return 0

        m = len(grid)  # number of rows
        n = len(grid[0])  # number of cols

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m - 1][n - 1] = grid[m - 1][n - 1]

        # initialize last row
        for c in range(n - 2, -1, -1):
            dp[m - 1][c] = grid[m - 1][c] + dp[m - 1][c + 1]

        # initialize last col
        for r in range(m - 2, -1, -1):
            dp[r][n - 1] = grid[r][n - 1] + dp[r + 1][n - 1]

        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])

        return dp[0][0]