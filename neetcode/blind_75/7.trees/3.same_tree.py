from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    """
    https://leetcode.com/problems/same-tree/
    https://www.youtube.com/watch?v=E36O5SWp-LE
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        res1 = self.isSameTree(p.left, q.left)
        res2 = self.isSameTree(p.right, q.right)

        if res1 and res2:
            return True
        else:
            return False
