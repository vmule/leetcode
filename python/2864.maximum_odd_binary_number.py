from collections import Counter


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        count = Counter(s)
        result = ["0"] * len(s)

        if count["1"] < 1:
            return ""

        elif count["1"] >= 1:
            count["1"] -= 1
            result[-1] = "1"

        for i in range(count["1"]):
            result[i] = "1"

        return "".join(result)
