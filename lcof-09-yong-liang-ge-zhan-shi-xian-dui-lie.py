class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        if len(self.stack2) > 0:
            while len(self.stack2) > 0:
                self.stack1.append(self.stack2.pop(-1))
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if len(self.stack1) > 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop(-1))
        if len(self.stack2) == 0:
            return -1
        return self.stack2.pop(-1)

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
