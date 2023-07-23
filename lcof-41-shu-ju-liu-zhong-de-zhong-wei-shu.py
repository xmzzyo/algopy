import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mx = []
        self.mi = []

    def addNum(self, num: int) -> None:
        if len(self.mx) != len(self.mi):
            heapq.heappush(self.mx, -num)
            heapq.heappush(self.mi, -heapq.heappop(self.mx))
        else:
            heapq.heappush(self.mi, num)
            heapq.heappush(self.mx, -heapq.heappop(self.mi))

    def findMedian(self) -> float:
        return -self.mx[0] if len(self.mx) != len(self.mi) else (self.mi[0] - self.mx[0]) / 2.



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()