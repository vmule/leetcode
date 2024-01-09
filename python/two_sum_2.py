from typing import List


class Solution:
    """
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for index, value in enumerate(numbers):
            diff = target - value
            if diff in seen:
                result = [seen[diff] + 1, index + 1]
                return result
            else:
                seen[value] = index
        return []
