from typing import List


class Solution:
    """
    https://leetcode.com/problems/unique-number-of-occurrences
    """

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countN = {}
        for e in arr:
            countN[e] = countN.get(e, 0) + 1

        count_values = countN.values()
        return len(count_values) == len(set(count_values))
