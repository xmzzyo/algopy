class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if len(self.stack2) > 0:
            return self.stack2.pop(-1)
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop(-1))
        return self.stack2.pop(-1)

    def peek(self) -> int:
        if len(self.stack2) > 0:
            return self.stack2[-1]
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop(-1))
        return self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
myQueue = MyQueue()
myQueue.push(1)
# myQueue.push(2)
# print(myQueue.peek())
print(myQueue.pop())
print(myQueue.stack1, myQueue.stack2)
print(myQueue.empty())
