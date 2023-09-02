class Solution:
    """
    https://leetcode.com/problems/length-of-last-word
    """

    def lengthOfLastWord(self, s: str) -> int:
        l_string = s.split()
        return len(l_string[-1])
