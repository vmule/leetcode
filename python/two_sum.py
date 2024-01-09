from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                result = [seen[diff], index]
                return result
            else:
                seen[num] = index
