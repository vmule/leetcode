from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        """
        https://leetcode.com/problems/rotate-array
        """
        i = k
        while i > 0:
            nums.insert(0, nums.pop())
            i = i - 1
        return nums
