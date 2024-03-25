from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        result = []

        for num in nums:
            idx = abs(num) - 1
            nums[idx] = abs(nums[idx]) * -1

        for index, num in enumerate(nums):
            if num > 0:
                result.append(index + 1)

        return result
