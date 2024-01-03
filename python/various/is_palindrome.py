import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join([i.lower() for i in s if (i.isalpha() or i.isnumeric())])
        return clean_s == clean_s[::-1]

    def isPalindrome2(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s.lower())
        return s == s[::-1]
