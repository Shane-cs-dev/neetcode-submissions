class Solution:
    """ This is the solution for two min-heap """
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort the meetings in ascending order
        meetings.sort(key=lambda x : (x[0], x[1]))

        # Create min heap for available room
        available = []
        count = [0] * n

        # Add each room into the min-heap
        for i in range(n):
            heapq.heappush(available, (0, i))
        
        for start, end in meetings:
            # Update the available room
            while available and available[0][0] < start:
                end_time, room = heapq.heappop(available)
                heapq.heappush(available, (start, room))
            # Get available room
            end_time, room = heapq.heappop(available)
            heapq.heappush(available, (end_time + (end - start), room))
            count[room] += 1

        # print(count)
        return count.index(max(count))
