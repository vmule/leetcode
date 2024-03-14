from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        k = goal
        result = 0
        curSum = 0
        prefixSums = {}
        prefixSums[0] = 1

        for n in nums:
            curSum += n
            diff = curSum - k

            result += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return result
