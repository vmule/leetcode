class Solution:
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        count = 0
        highest = 0
        for i in range(len(s)):
            if s[i] in seen:
                count = 1
            else:
                seen.append(s[i])
                count = count + 1
                highest = max(highest, count)
        return highest
