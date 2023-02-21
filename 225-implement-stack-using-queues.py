class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        if len(self.queue1) > 0:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def pop(self) -> int:
        if len(self.queue1) > 0:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)
        if len(self.queue2) > 0:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop(0)

    def top(self) -> int:
        top_data = self.pop()
        self.push(top_data)
        return top_data

    def empty(self) -> bool:
        return len(self.queue1) == 0 and len(self.queue2) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.queue1, obj.queue2)
print(obj.pop())
print(obj.queue1, obj.queue2)
print(obj.empty())
