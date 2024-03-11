from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:

        n = len(order)
        s_map = defaultdict(str)
        order_map = defaultdict(int)

        for index, value in enumerate(order):
            order_map[value] = index

        for i in s:
            if i not in order_map:
                s_map[n] += i
            else:
                index = order_map[i]
                s_map[index] += i

        result = ""
        for i in range(n + 1):
            result += s_map[i]
        return result
