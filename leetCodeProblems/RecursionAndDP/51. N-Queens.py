"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

Input: n = 1
Output: [["Q"]]

"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        self.result = []

        def generate_results(state):
            ans = []
            for row in state:
                ans.append(''.join(row))
            self.result.append(list(ans))

        def backtrack(row, columns, diagonal, anti_diagonal, state):
            if row == n:
                generate_results(state)
                return

            # given row, try to place at each col
            for col in range(n):
                current_diag = row + col
                current_anti_diag = row - col

                if col in columns or current_diag in diagonal or current_anti_diag in anti_diagonal:
                    continue

                # place the queen
                columns.add(col)
                diagonal.add(current_diag)
                anti_diagonal.add(current_anti_diag)
                state[row][col] = 'Q'

                # go to next row
                backtrack(row + 1, columns, diagonal, anti_diagonal, state)

                # remove the queen
                columns.remove(col)
                diagonal.remove(current_diag)
                anti_diagonal.remove(current_anti_diag)
                state[row][col] = '.'

        board = [['.'] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), board)

        return self.result