from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # use DFS algo
        def valid(node, lower_bound, upper_bound):
            if not node:
                return True
            if not (node.val < upper_bound and node.val > lower_bound):
                return False

            return valid(
                node.left, lower_bound=lower_bound, upper_bound=node.val
            ) and valid(node.right, lower_bound=node.val, upper_bound=upper_bound)

        result = valid(root, lower_bound=float("-inf"), upper_bound=float("inf"))
        return result
