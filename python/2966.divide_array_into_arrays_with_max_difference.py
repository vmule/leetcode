from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        nums.sort()
        result = [nums[i : i + 3] for i in range(0, len(nums), 3)]

        for element in result:
            if element[-1] - element[0] > k:
                return []
        return result
