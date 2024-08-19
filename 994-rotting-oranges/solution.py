from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        oranges = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    oranges += 1

        mins = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q and oranges < 0:
            mins += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for i, j in directions:
                    r, c = row + i, col + j
                    if (
                        r < 0
                        or c < 0
                        or r >= len(grid)
                        or c >= len(grid[row])
                        or grid[r][c] != 1
                    ):
                        continue
                    grid[r][c] = 2
                    q.append((r, c))
                    oranges -= 1

        return mins if oranges == 0 else -1
