from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        nums.append(float("-inf"))

        i = 1
        while i < len(nums) - 1:
            if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
                return i
            i += 1
        return 0
