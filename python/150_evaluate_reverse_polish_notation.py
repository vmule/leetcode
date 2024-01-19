from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens:
            if n == "+":
                result = stack.pop() + stack.pop()
            elif n == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                result = num1 - num2
            elif n == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                result = int(num1 / num2)
            elif n == "*":
                result = stack.pop() * stack.pop()
            else:
                result = int(n)
            stack.append(result)
        return stack[0]
