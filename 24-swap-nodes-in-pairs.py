# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        p, q = head, head.next
        cur_head = q
        while True:
            tmp = q.next
            q.next = p
            if tmp is None or tmp.next is None:
                p.next = tmp
                break
            p.next = tmp.next
            p, q = tmp, tmp.next
            # print_list(cur_head)
        return cur_head

    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy_head = ListNode()
        dummy_head.next = head
        cur = dummy_head
        while cur.next and cur.next.next:
            tmp = cur.next.next.next
            tmp1 = cur.next
            cur.next = cur.next.next
            cur.next.next = tmp1
            cur.next.next.next = tmp
            cur = cur.next.next
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
    print_list(Solution().swapPairs(head))
