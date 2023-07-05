# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def rob_tree(cur):
            if cur is None:
                return [0, 0]
            left = rob_tree(cur.left)
            right = rob_tree(cur.right)
            val1 = cur.val + left[0] + right[0]
            val2 = max(left[0], left[1]) + max(right[0], right[1])
            return [val2, val1]
        return max(rob_tree(root))
