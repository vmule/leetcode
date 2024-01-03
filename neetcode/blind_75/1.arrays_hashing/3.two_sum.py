from typing import List


class Solution:
    """
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index = 0
        result = []
        for index, _ in enumerate(numbers):
            rem = target - numbers[index]
            tmp = numbers[index]
            # -1000 <= numbers[i] <= 1000
            numbers[index] = 9999
            if rem in numbers:
                result.append(index + 1)
                result.append(numbers.index(rem) + 1)
                return result
            numbers[index] = tmp
        return []
