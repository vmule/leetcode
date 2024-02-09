import math
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        count = {}
        result = 0

        for i in nums:
            count[i] = count.get(i, 0) + 1

        for element in count:
            if count[element] == 1:
                return -1
            result += math.ceil(count[element] / 3)

        return result
