class MedianFinder:

    def __init__(self):
        self.small, self.large = [], [] # Using max heap for small, and use min heap for large

    def addNum(self, num: int) -> None:
        # Decide where should we push the given number to
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        # Check the balance between two heap
        if len(self.small) > len(self.large) + 1:
            popped_num = heapq.heappop(self.small)
            heapq.heappush(self.large, -popped_num)
        elif len(self.large) > len(self.small) + 1:
            popped_num = heapq.heappop(self.large)
            heapq.heappush(self.small, popped_num)
        return

    def findMedian(self) -> float:
        # Corner case:
        if not self.small and not self.large:
            return None
        # If the length of both array are same
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]
        