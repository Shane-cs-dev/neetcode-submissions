class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort the intervals in ascending order
        intervals.sort()
        min_heap = [] # Store the available interval sorted by it length
        res = {} # Map the queries to the start_time

        # Loop through the queries
        i = 0
        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(min_heap, (end - start + 1, end))
                i += 1
            
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            res[query] = min_heap[0][0] if min_heap else -1
        # print(res)
        return [res[q] for q in queries]