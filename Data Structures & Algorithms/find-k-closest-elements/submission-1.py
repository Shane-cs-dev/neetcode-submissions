from collections import deque

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Sliding window
        queue = deque()
        for i in range(len(arr)):
            # Define current number
            cur_num = arr[i]
            # Check if the window is valid
            if len(queue) >= k and abs(queue[0] - x) > abs(cur_num - x):
                queue.popleft()
                queue.append(cur_num)
            elif len(queue) < k:
                queue.append(cur_num)
        
        return list(queue)
