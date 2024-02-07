class Solution:
    def frequencySort(self, s: str) -> str:

        count = {}
        result = ""

        for e in s:
            count[e] = count.get(e, 0) + 1

        for e in sorted(count, key=count.get, reverse=True):
            result += e * count[e]
        return result
