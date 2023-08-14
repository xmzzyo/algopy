# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        p = head
        random_dict = {}
        while p:
            random_dict[p] = Node(p.val)
            p = p.next
        p = head
        while p:
            random_dict[p].next = random_dict.get(p.next)
            random_dict[p].random = random_dict.get(p.random)
            p = p.next
        return random_dict[head]


