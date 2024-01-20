from typing import List


class Solution:
    """
    https://leetcode.com/problems/longest-common-prefix/
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        sorted_strs = sorted(strs)

        first = sorted_strs[0]
        last = sorted_strs[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return answer
            answer += first[i]
        return answer
