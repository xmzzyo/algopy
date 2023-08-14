# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        stack = []
        cur = root
        while cur or len(stack) > 0:
            if cur.left:
                stack.append(cur)
            else:
                p = stack.pop(-1)
                if p.right:
                    stack.append(p.right)
        for i in range(len(stack) - 1):
            stack[i].right = stack[i + 1]
            stack[i + 1].left = stack[i]
        stack[-1].right = stack[0]
        stack[0].left = stack[-1]
        return stack[0]
