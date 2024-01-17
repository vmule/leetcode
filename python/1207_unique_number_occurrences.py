from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for element in arr:
            count[element] = count.get(element, 0) + 1

        count_uniq = set(count.values())

        return len(count) == len(count_uniq)
