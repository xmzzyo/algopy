# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and head.val == val:
            head = head.next
        if head is None:
            return None
        # dummy_head = ListNode(next=head) #添加一个虚拟节点
        i, j = head, head.next
        while j is not None:
            if j.val == val:
                i.next = j.next
            else:
                i = i.next
            j = j.next
        # print_list(head)
        return head


def build_list():
    head = ListNode()
    tmp = head
    for i in [7, 7, 7, 7, 7]:
        tmp.val = i
        tmp.next = ListNode()
        tmp = tmp.next
    # print_list(head)
    return head


def print_list(head):
    while head.next is not None:
        print(head.val, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    head = build_list()
    Solution().removeElements(head, 7)
