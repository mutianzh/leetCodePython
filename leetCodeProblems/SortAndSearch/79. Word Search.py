"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if self.backtrack(r, c, word):
                    return True

        return False

    def backtrack(self, r, c, suffix):

        if len(suffix) == 0:
            # all characters match
            return True

        if r < 0 or r == self.ROWS or c < 0 or c == self.COLS or self.board[r][c] != suffix[0]:
            return False

        self.board[r][c] = "#"
        for r_offset, c_offset in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if self.backtrack(r + r_offset, c + c_offset, suffix[1:]):
                return True
        self.board[r][c] = suffix[0]

        return False
