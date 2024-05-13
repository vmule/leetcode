from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        for row in range(ROWS):
            if grid[row][0] == 0:
                for col in range(COLS):
                    if grid[row][col] == 1:
                        grid[row][col] = 0
                    else:
                        grid[row][col] = 1

        for col in range(COLS):
            one_count = 0
            for row in range(ROWS):
                if grid[row][col] == 1:
                    one_count += 1
            if one_count < ROWS - one_count:
                for row in range(ROWS):
                    if grid[row][col] == 1:
                        grid[row][col] = 0
                    else:
                        grid[row][col] = 1

        result = 0
        for row in range(ROWS):
            for col in range(COLS):
                result += grid[row][col] << (COLS - 1 - col)
        return result
