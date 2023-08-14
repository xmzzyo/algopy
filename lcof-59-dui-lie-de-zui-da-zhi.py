class MaxQueue:

    def __init__(self):
        self.q = []
        self.max_v = []

    def max_value(self) -> int:
        return self.max_v[0] if self.max_v else -1

    def push_back(self, value: int) -> None:
        self.q.append(value)
        while self.max_v and self.max_v[-1] < value:
            self.max_v.pop(-1)
        self.max_v.append(value)

    def pop_front(self) -> int:
        if not self.q:
            return -1
        top = self.q.pop(0)
        if top == self.max_v[0]:
            self.max_v.pop(0)
        return top

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
