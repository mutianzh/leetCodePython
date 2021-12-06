"""
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.
"""
import collections

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = collections.defaultdict(int)
        for row in matrix:
            combination = []
            for c in row:
                combination.append(c ^ row[0])

            key = tuple(combination)
            count[key] += 1

        return max(count.values())