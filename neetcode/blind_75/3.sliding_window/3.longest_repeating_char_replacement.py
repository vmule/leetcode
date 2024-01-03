class Solution:
    """
    https://leetcode.com/problems/longest-repeating-character-replacemen
    """

    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        result = 0
        key_counts = {}

        for r in range(len(s)):
            key_counts[s[r]] = 1 + key_counts.get(s[r], 0)

            while (r - l + 1) - max(key_counts.values()) > k:
                key_counts[s[l]] -= 1
                l += 1

            result = max(result, (r - l + 1))

        return result
