class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        if self.len <= index:
            return -1
        head = self.head
        while index > 0:
            head = head.next
            index -= 1
        return head.val

    def addAtHead(self, val: int) -> None:
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        self.len += 1

    def addAtTail(self, val: int) -> None:
        if self.len == 0:
            self.addAtHead(val)
            return
        new_tail = Node(val)
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = new_tail
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return
        if index > self.len:
            return
        p = self.head
        while index > 1:
            p = p.next
            index -= 1
        p_next = p.next
        new_node = Node(val)
        p.next = new_node
        new_node.next = p_next
        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.len:
            return
        if index == 0:
            self.head = self.head.next
            self.len -= 1
            return
        p = self.head
        while index > 1:
            p = p.next
            index -= 1
        p.next = p.next.next if p.next is not None else None
        self.len -= 1


def print_list(head):
    if head is None:
        return
    while head.next is not None:
        print(head.val, end="->")
        head = head.next
    print(head.val)


if __name__ == "__main__":
    # Your MyLinkedList object will be instantiated and called as such:
    linkedList = MyLinkedList()
    print_list(linkedList.head)
    linkedList.addAtIndex(1, 0)
    print_list(linkedList.head)
    print(linkedList.get(0))
    exit()
    linkedList.addAtHead(1)
    print_list(linkedList.head)
    linkedList.deleteAtIndex(0)
    print_list(linkedList.head)
    linkedList.addAtTail(3)
    print_list(linkedList.head)
    linkedList.addAtIndex(1, 2)
    print_list(linkedList.head)
    print(linkedList.get(1))
    print_list(linkedList.head)
    linkedList.deleteAtIndex(1)
    print_list(linkedList.head)
    print(linkedList.get(1))
