from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value])
        return

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timeMap:
            values = self.timeMap[key]
            result = self.binary_search(values, timestamp)
            return result
        else:
            return ""

    def binary_search(self, _list, target):
        l = 0
        r = len(_list) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if _list[mid][0] <= target:
                res = _list[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
