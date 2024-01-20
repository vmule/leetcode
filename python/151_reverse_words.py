class Solution:
    """
    https://leetcode.com/problems/reverse-words-in-a-string/
    """

    def reverseWords(self, s: str) -> str:
        a = s.split()
        return " ".join(a[::-1])
