# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow, fast = head, head.next
        if fast.next is None:
            return None
        dis1, dis2 = 0, 1
        flag = False
        while fast:
            if slow == fast:
                flag = True
                break
            slow = slow.next
            if fast.next is None:
                return None
            fast = fast.next.next
            dis1 += 1
            dis2 += 2
        if not flag:
            return None
        circle_len = dis2 - dis1
        p, q = head, head
        while circle_len > 0:
            q = q.next
            circle_len -= 1
        while True:
            if p == q:
                return p
            p = p.next
            q = q.next


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
