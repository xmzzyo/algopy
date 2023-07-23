# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        path = []
        stack = []
        cur = root
        while cur is not None or len(stack) > 0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                path.append(cur.val)
                stack.append(cur.right)
                cur = cur.right
        print(path)
        for i in range(len(path) - 1):
            if not path[i] < path[i + 1]:
                return False
        return True
