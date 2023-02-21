# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d = 0
        if root is None:
            return d
        q = [root]
        while len(q) > 0:
            cur_len = len(q)
            while cur_len > 0:
                cur = q.pop(0)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                cur_len -= 1
            d += 1
        return d

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        d = 0
        if root is None:
            return d

        def depth(cur):
            if cur is None:
                return 0
            return max(1 + depth(cur.left), 1 + depth(cur.right))

        return depth(root)
