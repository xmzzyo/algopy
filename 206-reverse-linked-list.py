# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_link_list(root):
    p, q = root, root.next
    p.next = None
    while q:
        q_next = q.next
        q.next = p
        p, q = q, q_next
    return p


def build_link_list(data):
    root = ListNode()
    root.val = data[0]
    p = root
    for i in data[1:]:
        node = ListNode()
        node.val = i
        p.next = node
        p = node
    return root


def print_link_list(root):
    while root:
        print(root.val, end="->")
        root = root.next
    print()


p = build_link_list([1, 2, 3, 4, 5, 6])
print_link_list(p)
p = reverse_link_list(p)
print_link_list(p)
exit()


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        p, q = head, head.next
        cur_head = head
        while q:
            q_next = q.next
            q.next = cur_head
            cur_head = q
            p.next = q_next
            # print_list(cur_head)
            q = p.next
        return cur_head

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        reversed = self.reverseList2(head.next)
        p = reversed
        while p.next:
            p = p.next
        p.next = head
        head.next = None
        return reversed


def build_list():
    head = ListNode()
    tmp = head
    for i in [1, 2, 3, 4, 5]:
        tmp.val = i
        tmp.next = ListNode()
        tmp = tmp.next
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
    head = build_list()
    print_list(head)
    print_list(Solution().reverseList2(head))
