class Solution:
    def romanToInt(self, s: str) -> int:

        mapping = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

        i = n = len(s) - 1
        result = 0

        while i >= 0:
            if i < n and mapping[s[i]] < mapping[s[i + 1]]:
                result -= mapping[s[i]]
            else:
                result += mapping[s[i]]
            i -= 1
        return result
