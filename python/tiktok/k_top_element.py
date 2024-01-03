from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for num, n_count in count.items():
            freq[n_count].append(num)

        output = []
        for i in range(len(freq) - 1, 0, -1):
            for value in freq[i]:
                output.append(value)
                if len(output) == k:
                    return output
