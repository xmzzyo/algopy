# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        stack = [root]
        while len(stack) > 0:
            cur = stack.pop(-1)
            res.append(cur.val)
            if cur.left is not None:
                stack.append(cur.left)
            if cur.right is not None:
                stack.append(cur.right)
        return res[::-1]
