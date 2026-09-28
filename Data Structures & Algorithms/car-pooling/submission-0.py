class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Sort the array trips by its starting point
        trips.sort(key= lambda x : x[1])
        
        # Create a min heap to track the end point and its capacity
        min_heap = [] # (end point, capacity)

        # Loop through the array trips
        cur_cap = 0
        for cap, start_point, end_point in trips:
            cur_cap += cap
            # Check if there's passenger we can drop
            while cur_cap > capacity and min_heap:
                last_end_point, last_cap = min_heap[0]
                if start_point >= last_end_point:
                    cur_cap -= last_cap
                    heapq.heappop(min_heap)
                else:
                    break
            # If the current capacity still exceed the overall capacity
            if cur_cap > capacity:
                return False
            # Else add the curent data into the min_heap
            else:
                heapq.heappush(min_heap, (end_point, cap))
        
        return True
