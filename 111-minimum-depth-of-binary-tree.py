# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        d = 1
        if root is None:
            return 0
        q = [root]
        while len(q) > 0:
            cur_len = len(q)
            while cur_len > 0:
                cur = q.pop(0)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                if cur.left is None and cur.right is None:
                    return d
                cur_len -= 1
            d += 1
        return d

    def minDepth2(self, root: Optional[TreeNode]) -> int:
        d = 0
        if root.left is None and root.right is None:
            return 0

        def depth(cur):
            if cur is None:
                return 0
            left_d = depth(cur.left)
            right_d = depth(cur.right)
            if cur.left is None and cur.right is not None:
                return 1 + right_d
            if cur.left is not None and cur.right is None:
                return 1 + left_d
            return 1 + min(depth(cur.left), depth(cur.right))

        return depth(root)
