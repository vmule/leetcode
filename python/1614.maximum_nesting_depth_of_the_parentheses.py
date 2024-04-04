class Solution:
    def maxDepth(self, s):
        count = 0
        max_count = 0
        for i in s:
            if i == "(":
                count += 1
            elif i == ")":
                count -= 1
            max_count = max(max_count, count)
        return max_count
