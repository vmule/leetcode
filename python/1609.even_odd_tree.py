from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([[root, 0]])
        current_value = 0
        current_level = 0

        while q:
            node, level = q.popleft()

            # even level
            if level % 2 == 0:
                # value should be odd
                if node.val % 2 == 0:
                    return False
                if level == current_level and node.val <= current_value:
                    return False
            else:
                if node.val % 2 != 0:
                    return False
                if level == current_level and node.val >= current_value:
                    return False
            current_level = level
            current_value = node.val

            if node.left:
                q.append([node.left, level + 1])
            if node.right:
                q.append([node.right, level + 1])
        return True
