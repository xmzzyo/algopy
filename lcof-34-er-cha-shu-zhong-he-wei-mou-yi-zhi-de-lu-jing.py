# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        path = [root.val]

        def dfs(node):
            if sum(path) == target and node.left is None and node.right is None:
                res.append(path.copy())
                return
            if node.left:
                path.append(node.left.val)
                dfs(node.left)
                path.pop(-1)
            if node.right:
                path.append(node.right.val)
                dfs(node.right)
                path.pop(-1)

        dfs(root)
        return res
