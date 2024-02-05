class Solution:
    def __init__(self):
        self.result = ""
        self.length = 0

    def checkPal(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > self.length:
                self.length = r - l + 1
                self.result = s[l : r + 1]
            l -= 1
            r += 1

    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            # odd length pals
            l = r = i
            self.checkPal(s, l, r)

            # even length pals
            l = i
            r = i + 1
            self.checkPal(s, l, r)

        return self.result
