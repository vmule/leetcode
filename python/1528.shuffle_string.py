from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        result = [""] * len(s)

        for i in range(len(s)):
            idx = indices[i]
            letter = s[i]
            result[idx] = letter
        return "".join(result)
