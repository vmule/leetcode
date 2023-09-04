from collections import Counter


class Solution:
    """
    https://leetcode.com/problems/ransom-note
    """

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote) - Counter(magazine) == {}
