from typing import List
from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            row, col = q.popleft()
            for i, j in directions:
                r = row + i
                c = col + j
                if (
                    r >= len(grid)
                    or c >= len(grid[row])
                    or r < 0
                    or c < 0
                    or grid[r][c] != inf
                ):
                    continue
                grid[r][c] = grid[row][col] + 1
                q.append((r, c))
