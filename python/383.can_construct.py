from collections import Counter


class Solution:
    """
    https://leetcode.com/problems/ransom-note
    """

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # return Counter(ransomNote) - Counter(magazine) == {}

        m_count = {}
        for char in magazine:
            m_count[char] = m_count.get(char, 0) + 1

        for char in ransomNote:
            if m_count.get(char, 0) > 0:
                m_count[char] -= 1
            else:
                return False
        return True
