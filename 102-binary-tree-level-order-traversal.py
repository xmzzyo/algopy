# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [root]
        res = []
        if root is None:
            return []
        while len(q) > 0:
            cur_len = len(q)
            cur_layer = []
            while cur_len > 0:
                cur = q.pop(0)
                cur_layer.append(cur.val)
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
                cur_len -= 1
            res.append(cur_layer)
        return res
