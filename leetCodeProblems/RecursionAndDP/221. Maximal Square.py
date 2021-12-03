"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:

Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:
Input: matrix = [["0"]]
Output: 0

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix) == 0:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        ans = 0
        dp = [[0] * col for _ in range(row)]
        for i in range(col):
            dp[0][i] = int(matrix[0][i])
            ans = max(ans, dp[0][i])

        for i in range(row):
            dp[i][0] = int(matrix[i][0])
            ans = max(ans, dp[i][0])

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                    ans = max(ans, dp[i][j])

        return ans ** 2