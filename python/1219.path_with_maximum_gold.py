from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] == 0:
                return 0
            tmp = grid[row][col]
            grid[row][col] = 0
            result = 0
            positions = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]

            for row2, col2 in positions:
                result = max(result, tmp + dfs(row2, col2))
            grid[row][col] = tmp
            return result

        result = 0
        for row in range(ROWS):
            for col in range(COLS):
                result = max(result, dfs(row, col))
        return result
