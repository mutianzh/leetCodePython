"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:
Input: n = 1
Output: [[1]]
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        if not n or n < 1:
            return []

        values = range(1, n ** 2 + 1, 1)
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        i = 0
        while left < right and top < bottom:
            for c in range(left, right):
                matrix[top][c] = values[i]
                i += 1

            for r in range(top, bottom):
                matrix[r][right] = values[i]
                i += 1

            for c in range(right, left, -1):
                matrix[bottom][c] = values[i]
                i += 1

            for r in range(bottom, top, -1):
                matrix[r][left] = values[i]
                i += 1

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        if i < len(values):
            for r in range(top, bottom + 1):
                for c in range(left, right + 1):
                    matrix[r][c] = values[i]
                    i += 1

        return matrix