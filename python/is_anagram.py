from collections import Counter


class Solution:
    """https://leetcode.com/problems/valid-anagram"""

    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}
        if len(s) != len(t):
            return False
        for i in range(len(s) - 1):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT

        # return Counter(s) == Counter(t)
        # return sorted(s) == sorted(t)
