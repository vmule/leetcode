from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        result = []

        for i in range(1, n - 1):
            temp_row = []
            for j in range(1, m - 1):
                temp = 0

                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        temp = max(temp, grid[k][l])

                temp_row.append(temp)
            result.append(temp_row)

        return result
