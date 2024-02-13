from typing import List


class Solution:

    def isPalindrome(self, word: str) -> bool:
        left = 0
        right = len(word) - 1

        while left < right:
            if word[left] == word[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

    def firstPalindrome(self, words: List[str]) -> str:

        for word in words:
            if self.isPalindrome(word):
                return word
        return ""
