class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1_dict = {}
        common = 0

        for char in text1:
            text1_dict[char] = text1_dict.get(char, 0) + 1

        for char in text2:
            if char in text1_dict and text1_dict[char] > 0:
                common += 1
                text1_dict[char] -= 1

        return common
