from collections import deque
from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Use BFS algorithm
        res = []
        q = deque()
        q.append(root)

        # while q is not empty
        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                node = q.popleft()
                # check if node is not None
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # check if level is not empty
            if level:
                res.append(level)
        return res
