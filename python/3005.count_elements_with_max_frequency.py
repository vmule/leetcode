from collections import defaultdict
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        count = defaultdict(int)
        buckets = defaultdict(list)

        for i in nums:
            count[i] += 1

        for char, cnt in count.items():
            buckets[cnt].append(char)

        most_frequent = max(buckets.keys())
        return most_frequent * len(buckets[most_frequent])
