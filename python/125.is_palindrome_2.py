class Solution:
    """
    https://leetcode.com/problems/valid-palindrome
    """

    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join([i.lower() for i in s if i.isalnum()])
        l, r = 0, len(clean_s) - 1

        while r > l:
            if clean_s[r] != clean_s[l]:
                return False
            l += 1
            r -= 1
        return True
