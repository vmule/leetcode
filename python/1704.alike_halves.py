class Solution:
    """
    https://leetcode.com/problems/determine-if-string-halves-are-alike
    """

    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(["a", "e", "i", "o", "u"])

        mid = len(s) // 2
        a1 = s[:mid]
        a2 = s[mid:]

        count1, count2 = 0, 0

        for i in range(len(a1)):
            if a1[i].lower() in vowels:
                count1 += 1
            if a2[i].lower() in vowels:
                count2 += 1
        return count1 == count2
