from typing import Dict
from typing import List
from typing import Set


class Solution:
    """
    https://leetcode.com/problems/top-k-frequent-elements
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for num, n_count in count.items():
            freq[n_count].append(num)

        output = []

        for value in freq[::-1]:
            for e in value:
                output.append(e)
                if len(output) == k:
                    return output
