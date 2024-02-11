from functools import cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        @cache
        def dfs(r, c1, c2):
            if c1 == c2 or min(c1, c2) < 0 or max(c1, c2) == COLS:
                return 0

            if r == ROWS - 1:
                return grid[r][c1] + grid[r][c2]

            res = 0
            for c1_d in [-1, 0, +1]:
                for c2_d in [-1, 0, +1]:
                    res = max(res, dfs(r + 1, c1 + c1_d, c2 + c2_d))
            res += grid[r][c1] + grid[r][c2]
            return res

        return dfs(0, 0, COLS - 1)


grid = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]

a = Solution()
a.cherryPickup(grid)
