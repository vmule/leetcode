from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = OrderedDict()
        for index, element in enumerate(s):
            if element in count:
                count[element] = float("inf")
            else:
                count[element] = index

        for value in count.values():
            if value < len(s):
                return value
        return -1
