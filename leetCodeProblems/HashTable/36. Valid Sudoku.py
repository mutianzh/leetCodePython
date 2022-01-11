"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        r_set = [set() for _ in range(N)]
        c_set = [set() for _ in range(N)]
        box_set = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                v = board[r][c]

                if v != ".":
                    # check row
                    if v in r_set[r]:
                        return False

                    r_set[r].add(v)

                    # check col
                    if v in c_set[c]:
                        return False

                    c_set[c].add(v)

                    # check box
                    index = r // 3 * 3 + c // 3
                    if v in box_set[index]:
                        return False

                    box_set[index].add(v)

        return True
