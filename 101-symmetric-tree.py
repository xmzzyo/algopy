# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        q = [root.left, root.right]
        while len(q) > 0:
            cur_l = q.pop(0)
            cur_r = q.pop(0)
            if cur_l is None and cur_r is None:
                continue
            if cur_l is None or cur_r is None or cur_l.val != cur_r.val:
                return False
            q.append(cur_l.left)
            q.append(cur_r.right)
            q.append(cur_l.right)
            q.append(cur_r.left)
        return True
