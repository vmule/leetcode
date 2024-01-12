from typing import List


class Solution:
    """
    https://leetcode.com/problems/string-compression
    """

    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:
            return len("1")

        i = 0
        j = 0

        while i < len(chars):
            initial_char = chars[i]
            count = 0
            while i < len(chars) and chars[i] == initial_char:
                count += 1
                i += 1
            chars[j] = initial_char
            j += 1
            if count > 1:
                for c in str(count):
                    chars[j] = c
                    j += 1
        return j
