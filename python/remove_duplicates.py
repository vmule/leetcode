from typing import List


class Solution:
    """
    https://leetcode.com/problems/remove-duplicates-from-sorted-array
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 2
        while r < len(nums):
            if nums[l] == nums[r]:
                nums.pop(r)
            else:
                l += 1
                r += 1
        return r
