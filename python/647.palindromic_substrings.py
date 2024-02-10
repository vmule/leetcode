class Solution:

    def countSubstrings(self, s: str) -> int:

        result = []
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result.append(s[left : right + 1])
                left -= 1
                right += 1

            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result.append(s[left : right + 1])
                left -= 1
                right += 1

        return len(result)
