from collections import Counter


class Solution:
    """https://leetcode.com/problems/valid-anagram"""

    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}
        if len(s) != len(t):
            return False
        for i in s:
            countS[i] = 1 + countS.get(i, 0)
        for i in t:
            countT[i] = 1 + countT.get(i, 0)
        return countS == countT

        # return Counter(s) == Counter(t)
        # return sorted(s) == sorted(t)
