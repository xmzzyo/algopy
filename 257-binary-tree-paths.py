# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [f"{root.val}"]
        l_paths = self.binaryTreePaths(root.left)
        r_paths = self.binaryTreePaths(root.right)
        paths = [f"{root.val}->{p}" for p in l_paths + r_paths]
        return paths
