from typing import List


class Solution:
    """
    https://leetcode.com/problems/contains-duplicate
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        return False
