# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def depth(cur):
            if cur is None:
                return 0
            ld = depth(cur.left)
            if ld == -1:
                return -1
            rd = depth(cur.right)
            if rd == -1:
                return -1
            if abs(ld - rd) > 1:
                return -1
            else:
                return 1 + max(ld, rd)

        return depth(root) != -1
