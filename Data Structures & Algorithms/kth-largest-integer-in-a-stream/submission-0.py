class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.limit = k
        self.min_heap = nums
        heapq.heapify(self.min_heap) # O(n)
        self.maintain()

    def maintain(self):
        while len(self.min_heap) > self.limit:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Add current item into the min_heap
        heapq.heappush(self.min_heap, val)
        self.maintain()
        return self.min_heap[0]