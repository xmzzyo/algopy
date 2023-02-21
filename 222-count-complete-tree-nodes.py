# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_d, right_d = 0, 0
        cur_l, cur_r = root.left, root.right
        while cur_l:
            cur_l = cur_l.left
            left_d += 1
        while cur_r:
            cur_r = cur_r.right
            right_d += 1
        if left_d == right_d:
            return pow(2, left_d + 1) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
