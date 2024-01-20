import random
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/maximum-depth-of-binary-tree
    https://www.youtube.com/watch?v=hTM3phVI6YQ
    """

    def recursiveMaxDepth(self, root):
        # using dfs
        if not root:
            return 0

        left_count = self.maxDepth(root.left)
        right_count = self.maxDepth(root.right)

        return 1 + max(left_count, right_count)

    def iterativeBFSMaxDepth(self, root):
        # using bfs
        if not root:
            return 0

        level = 0

        q = deque([root])
        while q:
            for _ in range(len(q)):
                root = q.popleft()
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            level += 1
        return level

    def iterativeDFSMaxDepth(self, root):
        # using dfs

        res = 0
        stack = [[root, 1]]

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result_1 = self.iterativeBFSMaxDepth(root)
        result_2 = self.recursiveMaxDepth(root)
        result_3 = self.iterativeDFSMaxDepth(root)

        if result_1 == result_2 == result_3:
            return random.choice([result_1, result_2, result_3])
