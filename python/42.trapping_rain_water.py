from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        MaxL, MaxR = height[L], height[R]
        water = 0

        while L < R:
            if height[L] <= height[R]:
                L += 1
                MaxL = max(MaxL, height[L])
                water += MaxL - height[L]
            else:
                R -= 1
                MaxR = max(MaxR, height[R])
                water += MaxR - height[R]
        return water
