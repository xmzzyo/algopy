# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        stack = [root]
        while len(stack) > 0:
            cur_len = len(stack)
            res.append(stack[-1].val)
            while cur_len > 0:
                p = stack.pop(0)
                if p.left:
                    stack.append(p.left)
                if p.right:
                    stack.append(p.right)
                cur_len -= 1
        return res
