from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len1, len2 = 0, 0
        p, q = headA, headB
        while p:
            len1 += 1
            p = p.next
        while q:
            len2 += 1
            q = q.next
        p, q = headA, headB
        while len1 > len2:
            p = p.next
            len1 -= 1
        while len2 > len1:
            q = q.next
            len2 -= 1
        while len1 > 0:
            if p == q:
                return p
            p = p.next
            q = q.next
        return None
