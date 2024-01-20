from typing import List


class Solution:
    def rotate_helper(self, nums: List[int], l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        l = 0
        r = len(nums) - 1
        self.rotate_helper(nums, l, r)

        l = 0
        r = k - 1
        self.rotate_helper(nums, l, r)

        l = k
        r = len(nums) - 1
        self.rotate_helper(nums, l, r)

        return nums
