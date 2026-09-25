class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Add the index information into the list and sort it by queue time
        for i, task in enumerate(tasks):
            task.append(i) # task: [queue time, process time, index]
        
        tasks.sort(key = lambda x : x[0]) # Sort the tasks by queue time in ascending order

        # Create a res and min heap to store the result and tasks when the time is available
        res, min_heap = [], []

        # Define a time 
        i, time = 0, tasks[0][0]

        while i < len(tasks) or min_heap:
            while i < len(tasks) and time >= tasks[i][0]: # When the time is valid for the task
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i += 1 # Push to the next available time

            # If there's still task available but the CPU is idle
            if not min_heap:
                time = tasks[i][0]
            
            else:
                process_time, idx = heapq.heappop(min_heap)
                time += process_time
                res.append(idx)
        
        return res

