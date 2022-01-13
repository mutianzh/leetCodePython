"""
Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while left < right and top < bottom:
            for i in range(left, right):
                result.append(matrix[top][i])

            for i in range(top, bottom):
                result.append(matrix[i][right])

            for i in range(right, left, -1):
                result.append(matrix[bottom][i])

            for i in range(bottom, top, -1):
                result.append(matrix[i][left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        # when while breaks, left == right or top == bottom
        # still possible that we have a single row or col left

        if len(result) < len(matrix) * len(matrix[0]):
            # still have a row or col left
            for c in range(left, right + 1):
                for r in range(top, bottom + 1):
                    result.append(matrix[r][c])

        return result