# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A is None and B is not None:
            return False
        if A is None and B is None:
            return True
        if B is None:
            return True
        if A.val == B.val:
            l = self.isSubStructure(A.left, B.left)
            r = self.isSubStructure(A.right, B.right)
            return l and r
        else:
            l = self.isSubStructure(A.left, B)
            r = self.isSubStructure(A.right, B)
            return l or r
