import heapq


class MedianFinder:

    def __init__(self):
        self.qmin = []
        self.qmax = []

    def addNum(self, num: int) -> None:
        if not self.qmin or num <= -self.qmin[0]:
            heapq.heappush(self.qmin, -num)
            if len(self.qmin) > len(self.qmax) + 1:
                heapq.heappush(self.qmax, -self.qmin[0])
        else:
            heapq.heappush(self.qmax, num)
            if len(self.qmax) > len(self.qmin) + 1:
                heapq.heappush(self.qmin, -self.qmax[0])

    def findMedian(self) -> float:
        if len(self.qmax) == len(self.qmin):
            return (self.qmax[0] + -self.qmin[0]) / 2
        else:
            return -self.qmin[0]





# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()