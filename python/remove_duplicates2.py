from typing import List


class Solution:
    """
    https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
    """

    def removeDuplicates2(self, nums: List[int]) -> int:
        i = 2
        while i < len(nums):
            if nums[i] == nums[i - 2]:
                nums.pop(i)
            else:
                i = i + 1
        return i
