from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # first value in preorder list is always the root

        # we find on which index of the inorder list is the root value,
        # anything that comes after that is our right subtree
        # anything that comes before that index is out left subtree

        # left subtree then is [:i] of inorder list
        # right subtree then is [i+1:] of inorder list

        # size of the subarray left tree - len(preorder) gives us where the right tree start
        # we find at which index the right tree start value is in the inorder list
        # i - 1 would be the left child
        # i + 1 would be the right child

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        for index, value in enumerate(inorder):
            if value == preorder[0]:
                break
        leftTreeLength = index

        root.left = self.buildTree(
            preorder[1 : leftTreeLength + 1], inorder[:leftTreeLength]
        )
        root.right = self.buildTree(
            preorder[leftTreeLength + 1 :], inorder[leftTreeLength + 1 :]
        )
        return root
