from typing import List


class Solution:
    """
    https://leetcode.com/problems/container-with-most-water/
    """

    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        solution = 0

        while l < r:
            area = (r - l) * min(height[r], height[l])
            solution = max(solution, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return solution
