from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        stack = [root]
        while len(stack) > 0:
            cur = stack.pop(-1)
            res.append(cur.val)
            if cur.right is not None:
                stack.append(cur.right)
            if cur.left is not None:
                stack.append(cur.left)
        return res

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:

        def traverse(cur):
            if cur is None:
                return []
            res = []
            res.append(cur.val)
            res.extend(traverse(cur.left))
            res.extend(traverse(cur.right))
            return res

        res = traverse(root)
        return res

