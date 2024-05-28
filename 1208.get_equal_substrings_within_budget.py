class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        curCost = 0
        left = 0
        right = 0
        result = 0

        while left <= right and right < len(s):
            curCost += abs(ord(s[right]) - ord(t[right]))

            while curCost > maxCost:
                curCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            result = max(result, (right - left + 1))
            right += 1

        return result
