from typing import List


class Solution:
    """
    https://leetcode.com/problems/longest-consecutive-sequence
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        length = 1
        set_nums = set(nums)

        for n in nums:
            if n - 1 in set_nums:
                pass
            else:
                tmp = n
                tmp_length = 1
                while (tmp + 1) in set_nums:
                    tmp_length += 1
                    tmp += 1
                length = max(length, tmp_length)
        return length
