# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        dummy_head = ListNode()
        dummy_head.next = head
        p, q = dummy_head, dummy_head.next
        for _ in range(n):
            q = q.next
        while q:
            q = q.next
            p = p.next
        p.next = p.next.next
        return dummy_head.next

def build_list(data):
    if len(data) == 0:
        return None
    head = ListNode(data[0])
    tmp = head
    for i in data[1:]:
        node = ListNode(i)
        tmp.next = node
        tmp = node
    # print_list(head)
    return head


def print_list(head):
    if head is None:
        return
    while head.next is not None:
        print(head.val, end="->")
        head = head.next
    print(head.val)


if __name__ == "__main__":
    head = build_list(data=[1, 2, 3])
    print_list(head)
    print_list(Solution().removeNthFromEnd(head, 3))
