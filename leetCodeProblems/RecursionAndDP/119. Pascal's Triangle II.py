"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        prev_row = [1]
        for i in range(1, rowIndex + 1):
            cur_row = [None for _ in range(i + 1)]
            cur_row[0] = 1
            cur_row[-1] = 1
            for j in range(1, i):
                cur_row[j] = prev_row[j - 1] + prev_row[j]

            prev_row = cur_row

        return prev_row