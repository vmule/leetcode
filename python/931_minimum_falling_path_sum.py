from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Bottom up DP

        n = len(matrix)

        for row in reversed(range(n - 1)):
            for col in range(n):
                lower_left = float("inf") if col == 0 else matrix[row + 1][col - 1]
                lower_right = float("inf") if col == n - 1 else matrix[row + 1][col + 1]
                lower_down = matrix[row + 1][col]

                matrix[row][col] += min(lower_left, lower_right, lower_down)

        return min(matrix[0])
