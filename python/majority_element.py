from typing import List


class Solution:
    """
    https://leetcode.com/problems/majority-element
    """

    def majorityElement(self, nums: List[int]) -> int:
        output = max(set(nums), key=nums.count)
        return output

        # Alternative solution

        # nums.sort()
        # n = len(nums)
        # return nums[n // 2]
