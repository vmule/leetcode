from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        diff = Counter(s) - Counter(t)

        total = 0
        for e in diff.values():
            total += e

        return total
