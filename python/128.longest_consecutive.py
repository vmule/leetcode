from typing import List


class Solution:
    """
    https://leetcode.com/problems/longest-consecutive-sequence
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        set_nums = set(nums)

        for n in nums:
            if n - 1 not in set_nums:
                length = 1
                while (n + length) in set_nums:
                    length += 1
                longest = max(longest, length)
        return longest
