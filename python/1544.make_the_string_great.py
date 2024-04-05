class Solution:
    def makeGood(self, s: str) -> str:

        my_stack = []

        for element in s:
            if my_stack and abs(ord(element) - ord(my_stack[-1])) == 32:
                my_stack.pop()
            else:
                my_stack.append(element)

        return "".join(my_stack)
