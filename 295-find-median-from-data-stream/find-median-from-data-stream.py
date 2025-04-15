class MedianFinder:

    def __init__(self):
        # let's min_heap bigger

        # store big half values
        self.min_heap = []
        # store small half values
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if self.max_heap and -self.max_heap[0] >= num:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.min_heap) > len(self.max_heap) + 1:
            transit_num = -heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, transit_num)

        if len(self.min_heap) < len(self.max_heap):
            transit_num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, transit_num)
        


    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return self.min_heap[0]