from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        if len(nums) == 1:
            return 1

        counts = defaultdict(int)
        result = 0
        size = 0
        left = 0

        for _, value in enumerate(nums):
            counts[value] += 1
            size += 1
            while counts[value] > k:
                left_val = nums[left]
                counts[left_val] -= 1
                left += 1
                size -= 1
            result = max(result, size)
        return result
