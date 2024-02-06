import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        k = k - 1
        while k:
            heapq._heapify_max(nums)
            k -= 1

        return nums[0]
