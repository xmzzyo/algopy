# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:

        def dfs(cur):
            if not cur:
                return
            dfs(cur.right)
            if self.k == 0:
                return cur.val
            self.k -= 1
            dfs(cur.left)

        self.k = k
        return dfs(root)
