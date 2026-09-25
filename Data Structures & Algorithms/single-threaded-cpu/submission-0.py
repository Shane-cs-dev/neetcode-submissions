class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Create a min heap to store a tuple (process_time, queue_time, index)
        min_heap = []

        # Loop through the task and add tuple into the min heap
        for i in range(len(tasks)):
            queue_time, process_time = tasks[i]
            heapq.heappush(min_heap, (process_time, queue_time, i))
        
        # Pop from the min_heap and append the index into the res
        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap))

        return res