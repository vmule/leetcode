from typing import List


class Solution:
    """
    https://leetcode.com/problems/monotonic-array
    """

    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        increasing = False
        decreasing = False

        if nums[0] < nums[-1]:
            increasing = True
        else:
            decreasing = True

        i = 1
        while i < len(nums):
            if increasing:
                if nums[i - 1] <= nums[i]:
                    i += 1
                else:
                    return False
            if decreasing:
                if nums[i - 1] >= nums[i]:
                    i += 1
                else:
                    return False
        return True
