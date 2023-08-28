from typing import List


class Solution:
    """
    https://leetcode.com/problems/remove-duplicates-from-sorted-array
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        print(nums)
        return len(nums)
