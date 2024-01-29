from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        total = 0
        res = 0

        count = defaultdict(int)

        for r in range(len(fruits)):
            count[fruits[r]] += 1

            total += 1

            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1
                total -= 1
                l += 1

                if count[f] == 0:
                    count.pop(f)

            res = max(res, total)
        return res
