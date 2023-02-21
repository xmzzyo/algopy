# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        stack = [root]
        while len(stack) > 0:
            cur_len = len(stack)
            cur_layer = []
            while cur_len > 0:
                cur = stack.pop(0)
                cur_layer.append(cur.val)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
                cur_len -= 1
            res.append(cur_layer)
        return res[::-1]
