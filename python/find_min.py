from typing import List


class Solution:
    """
    https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
    """

    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        l, r = 0, (len(nums) - 1)

        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break

            m = (l + r) // 2
            result = min(result, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1

            else:
                r = m - 1

        return result
