from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(openCount, closeCount):
            print(stack)
            if openCount == closeCount == n:
                result.append("".join(stack))
                return

            if openCount < n:
                stack.append("(")
                backtrack(openCount + 1, closeCount)
                stack.pop()

            if closeCount < openCount:
                stack.append(")")
                backtrack(openCount, closeCount + 1)
                stack.pop()

        backtrack(0, 0)

        return result


a = Solution()

a.generateParenthesis(3)
