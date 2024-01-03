from typing import List


class Solution:
    """
    https://leetcode.com/problems/valid-parentheses/
    """

    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        for i in s:
            if i == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif i == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif i == "}" and stack and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0
