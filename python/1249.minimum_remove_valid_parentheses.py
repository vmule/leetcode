class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_list = list(s)
        stack = []

        for i, char in enumerate(s_list):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    s_list[i] = ""
        while stack:
            i = stack.pop()
            s_list[i] = ""

        return "".join(s_list)
