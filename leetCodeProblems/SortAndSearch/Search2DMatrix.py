"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])

        if matrix[0][0] > target or matrix[m - 1][n - 1] < target:
            return False

        length = m * n
        low = 0
        high = m * n - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            row = int(mid / n)
            col = int(mid % n)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False