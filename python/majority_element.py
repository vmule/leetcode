from typing import List


class Solution:
    """
    https://leetcode.com/problems/majority-element
    """

    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n // 2]
