"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and space is marked as 1 and 0 respectively in the grid.
Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if not obstacleGrid:
            return 0

        m = len(obstacleGrid)  # number of rows
        n = len(obstacleGrid[0])  # number of cols

        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        dp = [[0 for _ in range(n)] for _ in range(m)]

        # initialize the last row
        set_to_zero = False
        for c in range(n - 1, -1, -1):
            if obstacleGrid[m - 1][c] == 1:
                set_to_zero = True

            dp[m - 1][c] = 0 if set_to_zero else 1

        # initialize the lasr col
        set_to_zero = False
        for r in range(m - 1, -1, -1):
            if obstacleGrid[r][n - 1] == 1:
                set_to_zero = True

            dp[r][n - 1] = 0 if set_to_zero else 1

        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r + 1][c] + dp[r][c + 1]

        return dp[0][0]

