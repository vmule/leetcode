class Solution:
    def scoreOfString(self, s: str) -> int:

        left = 0
        right = 1
        result = 0

        while right < len(s):
            result += abs(ord(s[left]) - ord(s[right]))
            left += 1
            right += 1
        return result
