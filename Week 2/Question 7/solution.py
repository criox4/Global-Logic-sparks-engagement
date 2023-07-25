import heapq

class Solution:
    def __init__(self):
        self.lower = []
        self.higher = []

    def balanceHeaps(self):
        # Balance the two heaps such that the difference in sizes is not more than one.
        if len(self.lower) > len(self.higher) + 1:
            element = -heapq.heappop(self.lower)
            heapq.heappush(self.higher, element)
        elif len(self.higher) > len(self.lower):
            element = heapq.heappop(self.higher)
            heapq.heappush(self.lower, -element)

    def getMedian(self):
        # Return the median of the data received till now.
        if len(self.higher) == len(self.lower):
            median = (self.higher[0] + (-self.lower[0])) / 2
        else:
            median = -self.lower[0]
        return median

    def insertHeaps(self, x):
        # Insert the value 'x' into the heaps and balance them.
        if not self.lower or x <= -self.lower[0]:
            heapq.heappush(self.lower, -x)
        else:
            heapq.heappush(self.higher, x)
        self.balanceHeaps()


