from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        # odd length palindromes can only have one element appearing odd times
        # even length palindromes will always have every element appearing even times

        count = defaultdict(int)
        odd = 0  # digits with odd count

        def dfs(node):
            nonlocal odd
            if not node:
                return 0

            count[node.val] += 1
            if count[node.val] % 2 == 1:
                odd_change = 1
            else:
                odd_change = -1
            odd += odd_change

            # reached a leaf node
            if not node.left and not node.right:
                if odd <= 1:
                    res = 1
                else:
                    res = 0
            else:
                # go to next level of the tree
                res = dfs(node.left) + dfs(node.right)
            odd -= odd_change
            count[node.val] -= 1
            return res

        return dfs(root)
