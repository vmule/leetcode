from typing import List


class Solution:
    """
    https://leetcode.com/problems/remove-element
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        try:
            while True:
                nums.remove(val)
        except ValueError:
            pass
        return len(nums)
