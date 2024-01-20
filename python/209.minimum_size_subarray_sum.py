from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = total = 0
        result = float("inf")

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                result = min((right - left + 1), result)
                print(left, right)
                total -= nums[left]
                left += 1

        if result < float("inf"):
            return result
        return 0
