"""
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles.
If it is not possible to find such walk return -1.
"""


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        seen = set()
        queue = collections.deque([(0, 0, 0, k)])  # steps taken, r, c, k left

        M = len(grid)  # num of rows
        N = len(grid[0])  # num of cols

        if k >= M + N - 2: return N + M - 2

        while queue:
            stp, r, c, k = queue.popleft()

            if r == M - 1 and c == N - 1:
                return stp

            # explore all neighbors:
            for dr, dc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if 0 <= dr and dr < M and 0 <= dc and dc < N and k - grid[dr][dc] >= 0:
                    new = (dr, dc, k - grid[dr][dc])
                    if new not in seen:
                        seen.add(new)
                        queue.append((stp + 1, dr, dc, k - grid[dr][dc]))

        return -1